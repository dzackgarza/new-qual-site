---
schema: qual/card@1
id: P-TRIV-PR08
kind: problem
title: Reliability of a five-relay bridge circuit
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The relay network is specified by Figure 7. Flash preserves only an image placeholder/caption, so the circuit topology needed to solve the probability problem is unresolved.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the missing-figure note with a description of the Figure 7 bridge circuit from Probability Problem 8 on page 27 of the source PDF.
---

::: {.problem}
Consider the circuit shown in figure.
Each of its five relays is closed with the probability $p$ independently of other relays.

(a) Find the probability that a signal will pass through the circuit.

(b) Find the probability that the relay $E$ is open if it is known that the signal has passed through the circuit.

Figure 7 of the source (the circuit) is a bridge: from the input the line splits into an upper branch through relay $A$ to an upper node and a lower branch through relay $C$ to a lower node; the upper node is joined to the output through relay $B$, the lower node is joined to the output through relay $D$, and relay $E$ joins the upper node to the lower node.
:::
