# Azure Cosmos DB for AI & Modern Applications

## Final Repository Structure

```
/
├── README.md                           # Main hack description (WhatTheHack format)
├── Coach/                              # Coach-only materials
│   ├── README.md                       # Coach guide with agenda and instructions
│   ├── Presentations/                  # Lecture slides for each topic
│   │   ├── Kickoff & Overview.pptx
│   │   ├── Cosmos DB Data Modeling & Optimization.pptx
│   │   ├── CosmosDBForAI.pptx
│   │   ├── Azure CosmosDB Security.pptx
│   │   └── Closing Session.pptx
│   ├── Reference/                      # Original lab materials for reference
│   │   ├── Modelling & Optimization lab.md
│   │   ├── SecurityHOL.md
│   │   └── Training_Agenda.md
│   └── Solutions/                      # Detailed solution guides
│       ├── Solution-00.md              # Prerequisites solution
│       ├── Solution-01.md              # Environment setup solution
│       ├── Solution-02.md              # Data modeling solution
│       ├── Solution-03.md              # AI search solution
│       └── Solution-04.md              # Security & cost optimization solution
└── Student/                            # Student-facing materials
    ├── Challenge-00.md                 # Prerequisites challenge
    ├── Challenge-01.md                 # Environment setup challenge
    ├── Challenge-02.md                 # Data modeling challenge
    ├── Challenge-03.md                 # AI search challenge
    ├── Challenge-04.md                 # Security & cost optimization challenge
    └── Resources/                      # All student resources
        ├── README.md                   # Resource usage instructions
        ├── banking-workshop/           # Complete banking application
        │   ├── backend/                # Python API service
        │   ├── frontend/               # Angular web app
        │   ├── infra/                  # Infrastructure as code
        │   ├── azure.yaml              # Azure Developer CLI config
        │   ├── lab1.md                 # Original deployment guide
        │   └── lab3.md                 # Original application guide
        └── Challenge02/                # Data modeling sample data
            ├── customers.json
            ├── products.json
            └── categories-and-tags.json
```

## Migration Summary

This repository has been successfully restructured from a traditional training format to the **What The Hack** challenge-based format. Here's what changed:

### Original Structure → New Structure

| Original | New Location | Purpose |
|----------|--------------|---------|
| `README.md` (training guide) | `README.md` (hack description) | Main hack introduction |
| `Lab-3/banking-workshop/` | `Student/Resources/banking-workshop/` | Application code and infrastructure |
| `Lab-3/banking-workshop/lab1.md` | Challenge-01.md | Environment setup challenge |
| `Lab-3/banking-workshop/lab3.md` | Challenge-03.md | AI search challenge |
| `Modeling & Optimization/lab.md` | Challenge-02.md | Data modeling challenge |
| `Security/SecurityHOL.md` | Challenge-04.md | Security & cost optimization |
| All `.pptx` files | `Coach/Presentations/` | Lecture materials for coaches |
| Original labs | `Coach/Reference/` | Reference materials |
| New content | `Coach/Solutions/` | Detailed solution guides |

### Key Improvements

1. **Challenge-Based Learning:** Converted prescriptive labs into discovery-based challenges with clear success criteria
2. **Coach Support:** Added comprehensive coach guides with solutions, troubleshooting, and teaching points
3. **Student Resources:** Organized all necessary files in a logical structure with clear instructions
4. **WhatTheHack Format:** Follows the established WhatTheHack template structure for consistency
5. **Self-Contained:** Each challenge builds on previous ones with proper navigation links

### Benefits of New Structure

- **Scalable:** Coaches can easily run this hack with multiple teams
- **Consistent:** Follows WhatTheHack standards for quality and format
- **Flexible:** Challenges can be customized based on time constraints
- **Educational:** Focus on discovery and understanding rather than step-by-step execution
- **Professional:** Production-ready skills rather than just tutorial completion

## Next Steps

1. **Test the Hack:** Run through all challenges end-to-end to validate the experience
2. **Coach Training:** Train coaches on the new format and solution guides
3. **Feedback Collection:** Gather feedback from initial hack runs to refine content
4. **Version Control:** Tag this as v1.0 of the restructured hack
5. **Documentation:** Update any external references to point to new structure

## Cleanup Recommendations

The following original directories can now be safely removed as their content has been migrated:
- `Kickoff & Overview/`
- `Lab-3/` (content moved to `Student/Resources/`)
- `Modeling & Optimization/` (content moved to `Coach/`)
- `Security/` (content moved to `Coach/`)
- Email `.msg` files (not needed for hack format)

This maintains the original content while providing a much better learning experience aligned with What The Hack principles.