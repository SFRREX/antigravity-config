# React Composition Patterns & Hooks Optimization (Vercel Labs Standards)

## 1. Avoid Boolean Prop Proliferation
Never create components with dozens of boolean flags (`isHeader`, `withFooter`, `hasIcon`, `isCompact`, `showBadge`). Use **Compound Components**:

```tsx
// ❌ Anti-pattern: Boolean prop sprawl
<Modal title="Edit Profile" showHeader showFooter isCompact hasCloseIcon />

// ✅ Clean Pattern: Compound Composition
<Modal>
  <Modal.Header>
    <Modal.Title>Edit Profile</Modal.Title>
    <Modal.CloseButton />
  </Modal.Header>
  <Modal.Body>
    <ProfileForm />
  </Modal.Body>
  <Modal.Footer>
    <Button variant="secondary">Cancel</Button>
    <Button variant="primary">Save</Button>
  </Modal.Footer>
</Modal>
```

## 2. Slot Pattern Over Render Props
Use explicit slots to allow custom styling and DOM placement without prop drilling:

```tsx
interface CardProps {
  children: React.ReactNode;
  headerAction?: React.ReactNode;
}

export function Card({ children, headerAction }: CardProps) {
  return (
    <div className="rounded-xl border border-zinc-800 bg-zinc-900/50 p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="font-semibold text-zinc-100">Overview</h3>
        {headerAction && <div>{headerAction}</div>}
      </div>
      <div>{children}</div>
    </div>
  );
}
```

## 3. Hooks Dependency & Memoization Invariants
- Do NOT wrap trivial expressions in `useMemo` or `useCallback` ($O(1)$ calculations cost more to memoize than re-evaluate).
- Only memoize:
  1. Expensive calculations (filtering/sorting 1,000+ items).
  2. Callbacks passed to memoized children (`React.memo`).
  3. Stable object references passed into `useEffect` dependency arrays.
