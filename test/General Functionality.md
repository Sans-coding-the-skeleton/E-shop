## Scenario 2: General Functionality (CRUD)

**Objective:** Verify Product and Order operations.
**Pre-conditions:** Application running.

1.  **Navigate:** Go to `http://127.0.0.1:5000/products`.
2.  **Add Product:** Fill form (Name: "Test Item", Price: 50.0) -> Submit.
3.  **Verify:** "Test Item" appears in the product list.
4.  **Create Order:** Go to `http://127.0.0.1:5000/orders`.
5.  **Action:** Click "Create Test Order".
6.  **Verify:** New order appears in the list with Status "pending".