---
schema: qual/card@1
id: P-WESTOP05-10
kind: problem
title: Lift multiplication to the universal cover of a topological group and prove associativity
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Part (a) refers to a source diagram that is missing from the retained Markdown. The text still identifies p as a covering map and asks for the based lifting criterion and uniqueness, so those roles are retained without reconstructing the original diagram layout.
---

::: {.problem}
1. Suppose $p:(E,e_0)\to(B,b_0)$ is a covering map and $f:(X,x_0)\to(B,b_0)$ is a based map, with the spaces in the source path-connected and locally path-connected. State necessary and sufficient conditions for a lift
   \[
   \widetilde f:(X,x_0)\to(E,e_0),
   \qquad p\circ\widetilde f=f,
   \]
   to exist. If it exists, determine how many such based lifts there are.
2. Let $G$ be a path-connected, locally path-connected topological group with identity $e$ and multiplication
   \[
   \mu:G\times G\to G,
   \]
   and let
   \[
   p:(H,e')\to(G,e)
   \]
   be a universal cover. Show that there is a map
   \[
   \mu':H\times H\to H
   \]
   satisfying
   \[
   p\circ\mu'=\mu\circ(p\times p).
   \]
3. Prove that $\mu'$ is associative.
:::
