# Hands-on Lab: Monitoring, Autoscale, and Security in Azure Cosmos DB

## Objective

This 1-hour lab guides you through monitoring Request Unit (RU) usage, switching to autoscale throughput, simulating workloads, and applying security best practices in Azure Cosmos DB.

---

## Section 1: Environment Setup

1. **Log in to Azure Portal**
   - Navigate to https://portal.azure.com and sign in.

2. **Create a Cosmos DB Account**
   - Select “Create a resource” > “Azure Cosmos DB for NoSQL”.
   - Choose a unique name and region.
   - Select “Provisioned throughput” and enable “Azure Cosmos DB for NoSQL API”.

3. **Create a Database and Container**
   - Database name: `RetailBankingDB`
   - Container name: `Transactions`
   - Partition key: `/customerId`
   - Throughput: Manual (400 RU/s)

---

## Section 2: Load Sample Data

1. **Open Data Explorer**
   - Navigate to your Cosmos DB account > Data Explorer.

2. **Insert Sample Documents**
   - Use the following schema:
     ```json
     {
       "transactionId": "TX123456789",
       "customerId": "CUST001",
       "accountId": "ACC987654321",
       "amount": 250.75,
       "timestamp": "2024-06-01T10:15:00Z",
       "merchant": "Amazon",
       "category": "Shopping"
     }
     ```
   - Insert at least 1000 documents with varied `customerId`, `accountId`, and `category` values.
   - Use bulk insert scripts or SDKs (Python, Node.js, .NET) if preferred.

---

## Section 3: Run Queries and Record Metrics

1. **Execute Queries in Data Explorer**
   - Query 1: Retrieve transactions by customer
     ```sql
     SELECT * FROM c WHERE c.customerId = "CUST001"
     ```
   - Query 2: Retrieve transactions by account
     ```sql
     SELECT * FROM c WHERE c.accountId = "ACC987654321"
     ```
   - Query 3: Retrieve transactions by category
     ```sql
     SELECT * FROM c WHERE c.category = "Shopping"
     ```

2. **Record Metrics**
   - For each query, note:
     - RU charge (shown in Query Metrics)
     - Latency (ms)
     - Any throttling events

3. **Monitor with Insights**
   - Go to “Insights” in your Cosmos DB account.
   - Review graphs for RU consumption, latency, and throttled requests.

4. **Enable Diagnostic Logs**
   - Go to “Diagnostic settings”.
   - Send logs to Log Analytics.
   - Use KQL to analyse RU usage over time.

---

## Section 4: Switch to Autoscale and Simulate Workload

1. **Navigate to Scale & Settings**
   - In your container, select “Scale & Settings”.

2. **Switch to Autoscale**
   - Click “Change throughput”.
   - Select “Autoscale” and set max RU/s (e.g., 4000 RU/s).
   - Save changes.

3. **Simulate Workload**
   - Use Data Explorer or SDK to run batch inserts and queries.
   - Observe how RU/s scales automatically in response to workload spikes.

4. **Monitor Autoscale Behaviour**
   - Return to “Insights” and watch RU/s usage graph.
   - Note how provisioned RU/s adjusts dynamically.

---

## Section 5: Security Configuration

### 5.1 Configure RBAC

1. Go to **Access control (IAM)** in your Cosmos DB account.
2. Assign roles:
   - “Cosmos DB Operator”
   - “Managed Identity Contributor”
   - Assign to your user or service principal.

### 5.2 Configure Private Endpoints

1. In **Networking**, add a private endpoint to restrict access to your VNet.
2. Validate connectivity from within your VNet.

### 5.3 Enable Encryption

1. Ensure data at rest is encrypted (default).
2. Optionally, configure customer-managed keys (CMK) for additional control.

---

## Section 6: Alerting and Cost Estimation

### 6.1 Configure Alerts for RU Consumption Spikes

1. Navigate to your Cosmos DB account in the Azure Portal.
2. Select **Alerts** under the Monitoring section.
3. Click **+ New alert rule**.
4. Set the **Scope** to your Cosmos DB account.
5. Under **Condition**, choose the signal **Total Request Units**.
6. Configure the threshold (e.g., greater than 3000 RU/s for 5 minutes).
7. Under **Action group**, create or select an action group to receive notifications (email, SMS, etc.).
8. Name the alert rule and click **Create alert rule**.

### 6.2 Calculate Request Charge

1. Use **Query Metrics** in Data Explorer to view the RU charge for each query.
2. The **Request Charge** indicates the number of RUs consumed by the operation.
3. For bulk operations, sum the RU charges across all requests to estimate total consumption.

### 6.3 Estimate Cost Using Pricing Calculator

1. Visit the [Azure Cosmos DB Capacity Calculator](https://cosmos.azure.com/capacitycalculator/).
2. Input your estimated RU/s and storage requirements.
3. Select **Autoscale** or **Manual** throughput mode.
4. Review the monthly cost estimate based on your configuration.

### 6.4 Peak vs Off-Peak Pricing Considerations

1. Azure Cosmos DB pricing is consistent across time; however, autoscale helps optimise costs during off-peak hours.
2. Autoscale automatically reduces provisioned RU/s during low usage periods, lowering your bill.
3. Use the [Azure Pricing Calculator](https://azure.microsoft.com/en-gb/pricing/calculator/) to model scenarios:
   - Peak: High RU/s for daytime operations
   - Off-peak: Reduced RU/s during nights/weekends
4. Compare monthly costs for manual vs autoscale configurations to determine the most cost-effective option.

---


## Section 6.5: Best Practices for Cost Optimisation in Azure Cosmos DB

To ensure efficient use of resources and minimise operational costs, consider the following best practices:

### 1. Partitioning Strategy
- Choose a partition key that ensures even data distribution and supports your most common query patterns.
- Avoid hot partitions by selecting high-cardinality keys (e.g., customerId, deviceId).
- Monitor partition skew using metrics in the Azure portal.

### 2. Indexing Policy Optimisation
- Use custom indexing policies to exclude properties that are not queried.
- Disable automatic indexing for write-heavy workloads and enable manual indexing as needed.
- Apply composite indexes for multi-property queries and sorting to reduce RU consumption.

### 3. Autoscale Throughput
- Use autoscale for workloads with variable or unpredictable traffic.
- Set an appropriate maximum RU/s to balance performance and cost.
- Monitor autoscale behaviour to ensure it aligns with usage patterns.

### 4. Time-to-Live (TTL)
- Enable TTL on containers or items to automatically delete stale data.
- Reduces storage costs and improves query performance by limiting dataset size.

### 5. Query Design
- Use SELECT specific fields instead of SELECT * to reduce RU charges.
- Avoid cross-partition queries when possible by including the partition key in filters.
- Use pagination (continuation tokens) for large result sets.

### 6. Monitoring and Alerts
- Enable diagnostic logs and send them to Log Analytics for detailed analysis.
- Set up alerts for high RU consumption, throttling, or storage growth.
- Use Azure Advisor and Cost Management tools to identify optimisation opportunities.

By following these practices, you can significantly reduce costs while maintaining performance and scalability in your Cosmos DB workloads.

----

## Section 7: Wrap-up & Recommendations

- Compare RU usage and latency before and after switching to autoscale.
- Discuss how autoscale impacts cost and performance for unpredictable workloads.
- Review security settings and validate restricted access.
- Summarise findings and best practices for monitoring, autoscale, and security in Cosmos DB.

---

## Clean Up

- Delete test containers and databases to avoid unnecessary charges.

---

**End of Lab**