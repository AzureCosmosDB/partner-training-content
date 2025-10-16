# What The Hack - Azure Cosmos DB for AI & Modern Applications - Coach Guide

## Introduction

Welcome to the coach's guide for the Azure Cosmos DB for AI & Modern Applications What The Hack. Here you will find links to specific guidance for coaches for each of the challenges.

This hack includes optional lecture presentations that feature short presentations to introduce key topics associated with each challenge. It is recommended that the host present each short presentation before attendees kick off that challenge.

**NOTE:** If you are a Hackathon participant, this is the answer guide. Don't cheat yourself by looking at these during the hack! Go learn something. :)

## Coach's Guides

- Challenge 00: **[Prerequisites - Ready, Set, GO!](./Solutions/Solution-00.md)**
  - Prepare development environment and Azure subscription access
- Challenge 01: **[Environment Setup & First Steps](./Solutions/Solution-01.md)**
  - Provision Cosmos DB accounts, configure basics, and validate connectivity
- Challenge 02: **[Data Modeling & Query Optimization](./Solutions/Solution-02.md)**
  - Design partitioned data models, write efficient queries, and analyze performance
- Challenge 03: **[AI-Powered Search with Vector Embeddings](./Solutions/Solution-03.md)**
  - Build AI agents with full-text, vector, and hybrid search capabilities
- Challenge 04: **[Security & Cost Optimization](./Solutions/Solution-04.md)**
  - Implement security best practices and cost-saving strategies

## Coach Prerequisites

Before coaching this hack, you should:

- Have experience with Azure Cosmos DB in production environments
- Understand NoSQL data modeling concepts and best practices
- Be familiar with AI/ML concepts, particularly vector embeddings and search
- Have hands-on experience with Azure OpenAI services
- Understand Azure security models and cost optimization strategies
- Be comfortable troubleshooting Azure services and application performance

## Azure Requirements

Coaches and students will need:

- Azure subscription with **Owner** rights
- Access to Azure OpenAI service
- Sufficient quota for:
  - GPT-4o: 30K tokens per minute
  - text-embedding-3-small: 5K tokens per minute
- Access to create Azure Cosmos DB accounts in multiple regions

## Suggested Hack Agenda

This hack is designed to be completed in 1 day (approximately 6-7 hours):

- **Day 1**
  - Welcome & Kickoff (30 mins)
  - Challenge 00: Prerequisites (30 mins)
  - Challenge 01: Environment Setup (90 mins)
  - **Break (15 mins)**
  - Challenge 02: Data Modeling (120 mins)
  - **Lunch Break (60 mins)**
  - Challenge 03: AI-Powered Search (120 mins)
  - **Break (15 mins)**
  - Challenge 04: Security & Cost Optimization (90 mins)
  - Wrap-up & Q&A (30 mins)

### Alternative 2-Day Format

For a more relaxed pace or deeper exploration:

- **Day 1**
  - Challenges 00-01 (3 hours with breaks)
  - Challenge 02 (2 hours)
- **Day 2**
  - Challenge 03 (2.5 hours with breaks)
  - Challenge 04 (2 hours)
  - Advanced topics and Q&A (30 mins)

## Coach Notes

### General Guidance

- Encourage students to work in teams of 3-5 people
- Each challenge builds on the previous one - ensure teams complete challenges in order
- Monitor Azure costs during the hack and help students clean up resources
- Be prepared to help with Azure OpenAI quota issues
- Have backup Azure subscriptions available if needed

### Common Challenges

1. **Azure OpenAI Access**: Some students may not have immediate access. Help them request access or provide temporary shared resources.

2. **Quota Limitations**: Azure OpenAI quota can be a bottleneck. Monitor usage and help students optimize their requests.

3. **Data Modeling Concepts**: Students may struggle with NoSQL thinking. Be ready to provide guidance on denormalization and embedding vs. referencing.

4. **Vector Search Understanding**: The concept of embeddings and similarity search may be new. Use analogies and visual explanations.

5. **Cost Optimization**: Help students understand the difference between provisioned and serverless throughput models.

### Key Teaching Points

- Emphasize the importance of understanding your data access patterns before designing your model
- Highlight the difference between RDBMS and NoSQL design approaches
- Explain how partition key choice affects performance and cost
- Demonstrate the power of combining different search types (full-text, vector, hybrid)
- Show real-world cost optimization techniques that can save significant money

## Repository Contents

- `./Coach`
  - Coach's Guide and related files
  - `/Solutions`
    - Solution files with completed example answers to each challenge
- `./Student`
  - Student's Challenge Guide
  - `/Resources`
    - Banking workshop application code
    - Infrastructure as Code templates
    - Sample data files
    - Presentation materials (provided to coaches for reference)

## Additional Resources

- [Azure Cosmos DB Documentation](https://docs.microsoft.com/azure/cosmos-db/)
- [Azure OpenAI Service Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/)
- [Azure Developer CLI Documentation](https://docs.microsoft.com/azure/developer/azure-developer-cli/)
- [Cosmos DB Best Practices](https://docs.microsoft.com/azure/cosmos-db/sql/best-practice-nosql)
- [Vector Search in Cosmos DB](https://docs.microsoft.com/azure/cosmos-db/sql/vector-search)