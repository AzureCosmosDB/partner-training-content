## Cosmos DB Data Modeling & Partitioning: Hands-On Lab

### Lab Objectives

- Understand how partition key and indexing choices impact cost and performance.
- Practically model and query an e-commerce dataset (Customers, Products, Categories, Tags, Sales Orders).
- Measure RU (Request Unit) consumption for different query patterns and data models.

---

### 1. **Setup: Prerequisites**

- Azure Subscription with Cosmos DB account (SQL API).
- Azure Portal or Azure CLI access.
- https://portal.azure.com/.
- (Optional) Azure Functions or SDK for automation.

---

### 2. **Lab Dataset: E-commerce Example**

#### **Entities**

- **Customer**
- **ProductCategory**
- **ProductTag**
- **Product**
- **SalesOrder**

#### **Sample JSON Documents**

```json
// Customer
{
  "id": "CUST001",
  "customerId": "CUST001",
  "type": "customer",
  "firstName": "Alice",
  "lastName": "Smith",
  "emailAddress": "alice@example.com",
  "addresses": [
    {
      "addressLine1": "123 Main St",
      "city": "Gurgaon",
      "country": "India"
    }
  ],
  "password": { "hash": "abc", "salt": "xyz" },
  "salesOrderCount": 2
}

// ProductCategory
{
  "id": "CAT001",
  "type": "category",
  "name": "Electronics"
}

// ProductTag
{
  "id": "TAG001",
  "type": "tag",
  "name": "Smartphone"
}

// Product
{
  "id": "PROD001",
  "categoryId": "CAT001",
  "categoryName": "Electronics",
  "sku": "ELEC-001",
  "name": "iPhone 15",
  "description": "Latest Apple smartphone",
  "price": 90000,
  "tags": [
    { "id": "TAG001", "name": "Smartphone" }
  ]
}

// SalesOrder
{
  "id": "SO001",
  "type": "salesOrder",
  "customerId": "CUST001",
  "details": [
    {
      "sku": "ELEC-001",
      "name": "iPhone 15",
      "price": 90000,
      "quantity": 1
    }
  ]
}
```

---

### 3. **Container Design Experiments**

#### **A. Customers & Sales Orders**

- **Container Name:** `customers`
- **Partition Key Option 1:** `/id`
- **Partition Key Option 2:** `/customerId`

**Steps:**
1. Create the container with `/id` as partition key.
2. Insert customer and sales order documents.
3. Run queries:
   - Retrieve customer by id.
   - Retrieve all sales orders for a customer.
4. Note RU consumption and latency.

**Repeat** with `/customerId` as partition key. Compare results.

---

#### **B. Products**

- **Container Name:** `products`
- **Partition Key Option 1:** `/categoryId`
- **Partition Key Option 2:** `/id`

**Steps:**
1. Create the container with `/categoryId` as partition key.
2. Insert product documents.
3. Run queries:
   - List all products in a category.
   - Retrieve product by id.
4. Note RU consumption and latency.

**Repeat** with `/id` as partition key. Compare results.

---

#### **C. Product Metadata (Categories & Tags)**

- **Container Name:** `productMeta`
- **Partition Key:** `/type` (value: `category` or `tag`)

**Steps:**
1. Create the container with `/type` as partition key.
2. Insert category and tag documents.
3. Run queries:
   - List all categories: `SELECT * FROM c WHERE c.type = 'category'`
   - List all tags: `SELECT * FROM c WHERE c.type = 'tag'`
4. Note RU consumption and latency.

---

### 4. **Indexing Policy Experiments**

- Default: All properties indexed.
- Custom: Exclude large or rarely queried properties.

**Steps:**
1. Modify indexing policy to exclude certain properties.
2. Run queries that include/exclude those properties.
3. Observe RU and performance impact.

---

### 5. **Query Patterns & Cost Analysis**

For each container/partition key/indexing setup:

- Run the following queries and record RU charge and latency:
  - **Point Read:** Retrieve by id or partition key.
  - **Range Query:** List all products in a category.
  - **Cross-Partition Query:** Query without partition key filter.
  - **Aggregation:** Count sales orders per customer.

**Sample Query:**
```sql
SELECT * FROM c WHERE c.customerId = 'CUST001' AND c.type = 'salesOrder'
```

**Record:**
| Container      | Partition Key | Query Type         | RU Charge | Latency (ms) | Notes                |
|----------------|--------------|--------------------|-----------|--------------|----------------------|
| customers      | /id          | Point Read         |           |              |                      |
| customers      | /customerId  | Range Query        |           |              |                      |
| products       | /categoryId  | List by Category   |           |              |                      |
| productMeta    | /type        | List all tags      |           |              |                      |

---

### 6. **Analysis & Recommendations**

- Which partition key provided the best balance for your workload?
- How did indexing changes affect RU and latency?
- Where did you observe hot partitions or cross-partition queries?
- What denormalisation or embedding strategies worked best?

---

### 7. **Cleanup**

- Delete containers/resources to avoid ongoing Azure costs.

---

### 8. **Further Learning & References**

- [CosmicWorks Sample](https://github.com/AzureCosmosDB/CosmicWorks)
- [Cosmos DB Partitioning Docs](https://aka.ms/cosmos-hierarchical-partitioning)
- [Request Units (RU) Explained](https://learn.microsoft.com/en-us/azure/cosmos-db/request-units)
- [Scaling Best Practices](https://learn.microsoft.com/en-us/azure/cosmos-db/scaling-provisioned-throughput-best-practices)

