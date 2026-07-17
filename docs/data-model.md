# Data model

The migration organizes identity, supplier master/performance/risk, components/programs/commodities, RFQs/quotes, versioned cost models, scenarios, awards, audit logs and cited AI conversations. UUIDs are used for entity keys; important records include timestamps or model versions. Supplier-user filtering must be enforced by supplier identity in every server query—not in the browser.
