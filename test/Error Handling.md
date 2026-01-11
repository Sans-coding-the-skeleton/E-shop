## Scenario 4: Error Handling

**Objective:** Verify transaction rollback.
1.  (Advanced) Temporarily modify `OrderRepository` to raise exception between Order Insert and Item Insert.
2.  Attempt to Create Order.
3.  **Expected:** "Transaction failed" in console. No partial order exists in `orders` table (Atomicity).