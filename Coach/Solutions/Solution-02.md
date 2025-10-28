# Challenge 02 - AI-Powered Search with Vector Embeddings - Coach's Guide

**[< Previous Challenge](./Solution-01.md)** - **[Home](../../README.md)** - **[Next Challenge >](./Solution-03.md)**

## Solution Overview

This challenge demonstrates how to build AI-powered applications using Azure Cosmos DB's vector search capabilities. Teams will explore a multi-agent banking system that combines traditional queries with AI-powered semantic search.

## Learning Objectives for Students

- Understand vector embeddings and semantic similarity search
- Learn how to combine traditional and AI-powered search patterns
- Experience multi-agent system architectures
- Practice with Azure OpenAI integration patterns
- Analyze the performance characteristics of vector searches

## Application Architecture Overview

### Multi-Agent System Components

1. **Coordinator Agent** (`coordinator_agent.prompty`)
   - Routes conversations to appropriate specialized agents
   - Maintains conversation context and state
   - Handles agent transitions and handoffs

2. **Customer Support Agent** (`customer_support_agent.prompty`)
   - Handles general inquiries and account information
   - Accesses customer data and transaction history
   - Provides account balance and status information

3. **Transactions Agent** (`transactions_agent.prompty`)
   - Processes money transfers and transactions
   - Validates account balances and limits
   - Updates account records in real-time

4. **Sales Agent** (`sales_agent.prompty`)
   - Handles product inquiries and recommendations
   - Uses vector search for banking offer recommendations
   - Provides personalized product suggestions

### Data Flow Architecture

```
User Query → Coordinator Agent → Specialized Agent → Cosmos DB + OpenAI → Response
```

## Detailed Solution Guide

### Part 1: Application Startup and Testing

#### Backend Service Startup
```bash
cd backend

# Linux/macOS
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate

pip install -r src/app/requirements.txt
```

**Expected Results:**
- Virtual environment created successfully
- All dependencies installed without errors
- Python service ready to start

#### Frontend Application Startup
```bash
cd frontend
npm install
ng serve --proxy-config proxy.conf.json
```

**Expected Results:**
- Angular application builds successfully
- Frontend accessible at `http://localhost:4200`
- Proxy configuration routes API calls to backend

### Part 2: Agent Coordination Testing

#### Money Transfer Scenario
**User Input:** \"I want to transfer money\"
**Expected Flow:**
1. Coordinator Agent receives request
2. Identifies transaction intent
3. Routes to Transactions Agent
4. Transactions Agent requests transfer details
5. User provides: \"500 from Acc001 to Acc003\"
6. Agent validates accounts and balances
7. Executes transfer and updates Cosmos DB
8. Confirms transaction completion

**Technical Implementation:**
```python
# Example transaction processing logic
def process_transfer(from_account, to_account, amount):
    # Validate accounts exist and have sufficient balance
    # Update account balances atomically
    # Record transaction history
    # Return confirmation details
```

**Validation Steps for Teams:**
1. Check conversation flow in browser
2. Verify agent handoff occurs correctly
3. Confirm transaction is recorded in Cosmos DB
4. Validate account balances are updated

### Part 3: Vector Search Testing

#### Banking Offers Scenario
**User Input:** \"Tell me about your banking offers\"
**Expected Flow:**
1. Coordinator Agent identifies product inquiry
2. Routes to Sales Agent
3. Sales Agent performs vector search on offers
4. Returns relevant banking products
5. User refines with \"credit card\"
6. Agent provides specific credit card offers

**Vector Search Implementation:**
```python
# Example vector search logic
def search_offers(query_text, similarity_threshold=0.7):
    # Generate embedding for user query
    embedding = openai_client.embeddings.create(
        input=query_text,
        model=\"text-embedding-3-small\"
    )
    
    # Perform vector search in Cosmos DB
    results = cosmos_client.query_items(
        query=\"SELECT * FROM c WHERE VectorDistance(c.embedding, @embedding) > @threshold\",
        parameters=[
            {\"name\": \"@embedding\", \"value\": embedding.data[0].embedding},
            {\"name\": \"@threshold\", \"value\": similarity_threshold}
        ]
    )
    return results
```

### Part 4: API Testing with Swagger

#### Direct API Testing
**Swagger URL:** `http://localhost:63280/docs`

**Sample Test Flow:**
1. **Create Session:**
   ```json
   POST /api/sessions
   {
     \"tenantId\": \"Contoso\",
     \"userId\": \"Mark\"
   }
   ```

2. **Send Message:**
   ```json
   POST /api/completions
   {
     \"tenantId\": \"Contoso\",
     \"userId\": \"Mark\",
     \"sessionId\": \"<session-id>\",
     \"message\": \"Hello there!\"
   }
   ```

**Expected Response Structure:**
```json
[
  {
    \"id\": \"<message-id>\",
    \"type\": \"ai_response\",
    \"sessionId\": \"<session-id>\",
    \"sender\": \"User\",
    \"text\": \"Hello there!\",
    \"tokensUsed\": 0
  },
  {
    \"id\": \"<response-id>\",
    \"type\": \"ai_response\",
    \"sessionId\": \"<session-id>\",
    \"sender\": \"Coordinator\",
    \"text\": \"Hi there! Welcome to our bank...\",
    \"tokensUsed\": 265
  }
]
```

## Common Coaching Challenges

### 1. Vector Search Concept Confusion
**Problem:** Teams don't understand how semantic similarity works
**Solutions:**
- Use concrete examples: \"credit card\" vs \"rewards program\"
- Show embedding visualization tools
- Explain cosine similarity in simple terms
- Demonstrate with similar vs dissimilar queries

### 2. Agent Handoff Not Working
**Problem:** Coordinator doesn't route to correct agents
**Solutions:**
- Check agent prompt templates for clarity
- Verify Azure OpenAI model is responding correctly
- Look at conversation logs in Debug container
- Ensure proper context is maintained

### 3. High RU Consumption
**Problem:** Vector searches consume many RUs
**Solutions:**
- Explain that vector searches are computationally expensive
- Show RU monitoring in Azure portal
- Discuss optimization strategies (caching, indexing)
- Compare with traditional query costs

### 4. Application Startup Issues
**Problem:** Frontend or backend won't start
**Solutions:**
- Check Node.js and Python versions
- Verify port availability (4200, 63280)
- Review dependency installation logs
- Ensure Azure services are running

## Performance Analysis Guide

### RU Consumption Patterns

**Traditional Queries:**
- Point reads: 1-3 RUs
- Range queries: 3-10 RUs
- Cross-partition queries: 10-50 RUs

**Vector Searches:**
- Simple vector query: 15-30 RUs
- Vector query with filters: 20-40 RUs
- Hybrid search (vector + text): 25-50 RUs

### Token Usage Monitoring

**Typical Token Consumption:**
- Simple queries: 50-200 tokens
- Complex conversations: 300-800 tokens
- Vector search with context: 200-500 tokens

**Coaching Points:**
- Show token usage in API responses
- Explain cost implications of token consumption
- Discuss optimization strategies

## Advanced Coaching Topics

### 1. Multi-Agent Architecture Patterns
- Explain agent specialization benefits
- Show how to design agent boundaries
- Discuss conversation state management
- Demonstrate error handling and recovery

### 2. Vector Search Optimization
- Explain embedding model selection
- Discuss similarity threshold tuning
- Show hybrid search implementation
- Cover vector index optimization

### 3. Real-World Scaling Considerations
- Discuss conversation state partitioning
- Explain agent load balancing
- Cover multi-tenant isolation
- Address security and compliance

## Troubleshooting Guide

### Application Issues
```bash
# Check backend service
curl http://localhost:63280/health

# Check frontend build
ng build --configuration development

# Review application logs
docker logs <container-name>
```

### Azure Service Issues
```bash
# Check OpenAI deployment status
az cognitiveservices account deployment list

# Check Cosmos DB connectivity
az cosmosdb sql database list

# Monitor RU consumption
# Use Azure portal Insights section
```

### Vector Search Issues
```python
# Test embedding generation
from openai import AzureOpenAI
client = AzureOpenAI(...)
response = client.embeddings.create(
    input=\"test query\",
    model=\"text-embedding-3-small\"
)
print(response.data[0].embedding[:5])  # First 5 dimensions
```

## Time Management

- **Total Duration:** 90-120 minutes
- **Application Setup:** 20 minutes
- **Basic Testing:** 30 minutes
- **Vector Search Exploration:** 40 minutes
- **API Testing:** 20 minutes
- **Analysis and Discussion:** 10 minutes

## Success Validation

Teams successfully complete when they can:
1. ✅ Start both frontend and backend applications
2. ✅ Demonstrate successful money transfer with agent coordination
3. ✅ Show vector search working for banking offers
4. ✅ Use Swagger API to test endpoints directly
5. ✅ Explain the difference between traditional and vector searches
6. ✅ Monitor and understand RU consumption patterns
7. ✅ Articulate how agent coordination works

## Key Teaching Moments

### 1. AI Integration Patterns
- Show how traditional databases integrate with AI services
- Explain the importance of prompt engineering
- Demonstrate context management in conversations

### 2. Vector Search Value Proposition
- Compare exact match vs semantic similarity
- Show real business value of intelligent search
- Discuss when to use vector vs traditional search

### 3. Multi-Agent System Benefits
- Explain specialization and modularity advantages
- Show how to handle complex business workflows
- Discuss scalability and maintainability benefits

## Preparation for Next Challenge

Before moving to Challenge 04:
- Ensure teams understand current cost implications
- Preview security concepts they'll implement
- Explain the importance of production readiness
- Set expectations for monitoring and optimization