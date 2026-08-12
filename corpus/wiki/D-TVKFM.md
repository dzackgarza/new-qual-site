---
schema: qual/card@1
id: D-TVKFM
kind: definition
title: "Topological Notions"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.definition title="Topological Notions"}
Let $X$ be a metric space and $A$ a subset.
Let $A'$ denote the limit points of $A$, and $\bar{A} \da A\union A'$ to be its closure.

- A **neighborhood** of $p$ is an open set $U_p$ containing $p$.

- An $\eps\dash$**neighborhood** of $p$ is an open ball $B_r(p) \da \ts{q \st d(p, q) < r}$ for some $r>0$.

- A point $p\in X$ is an **accumulation point** or a **limit point** of $A$ iff every *punctured* neighborhood $U_p\sm\ts{p}$ contains a point $q\in A$, so $q\neq p$.

- If $p\in A$ and $p$ is not a limit point of $A$, then $p$ is an **isolated point** of $A$.

- $A$ is **closed**  iff $A' \subset A$, so $A$ contains all of its limit points.

- A point $p\in A$ is **interior** iff there is a neighborhood $U_p \subset A$ that is strictly contained in $A$.

- $A$ is **open** iff every point of $A$ is interior.

- $A$ is **perfect** iff $A$ is closed and $A\subset A'$, so every point of $A$ is a limit point of $A$.

- $A$ is **bounded** iff there is a real number $M$ and a point $q\in X$ such that $d(p, q) < M$ for all $p\in A$.

- $A$ is **dense** in $X$ iff every point $x\in X$ is either a point of $A$, so $x\in A$, or a limit point of $A$, so $x\in A'$.
  I.e., $X\subset A\union A'$.

  - Alternatively, $\bar{A} = X$, so the closure of $A$ is $X$.
:::
