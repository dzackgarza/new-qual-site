---
schema: qual/card@1
id: P-6OVVU
kind: problem
title: "Main Idea: Using a funky deformation retract."
classification:
  areas:
  - topology
  topics:
  - retracts
  - homotopy
relations: []
review: draft
solved: false
---

::: problem
6. **Main Idea**: Using a funky deformation retract.
   See Hatcher, PDF page 55, Example 1.23. Add picture!!

Deformation retract $\\R^3 - S^1$ onto $S^2 - U$, where $U$ is a diameter inside $S^2$ also passing through the middle of $S^1$ in the interior.
This can be done by moving points outside of $S^2$ towards the surface, and points inside $S^2$ just move away from the $S^1$ inside (either towards $U$ or towards the surface of $S^2$, so they don't hit $S^1$).

Then take a geodesic between the endpoints of the diameter on $S^2$, pick any point $p$ on the geodesic, and move both diameter points towards it.
This yields $S^2 \vee S^1$ at the point $p$.
:::
