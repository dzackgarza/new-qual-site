---
schema: qual/card@1
id: E-AMD-DI5UYFIZ
kind: exercise
title: $-1$ is the unique element of order $2$ in the quaternion group
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Group Presentations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that the Quaternion group has only one element of order 2, namely $-1$.
:::

::: solution
**Goal:** Prove that in the quaternion group $Q_8$, the element $-1$ is the unique element of order $2$.

<1>1. Elements and presentation of $Q_8$:
    The quaternion group of order $8$ has elements:
    $$Q_8 = \{1, -1, i, -i, j, -j, k, -k\},$$
    subject to the defining relations:
    $$i^2 = j^2 = k^2 = ijk = -1, \quad (-1)^2 = 1, \quad (-1)g = g(-1) = -g \text{ for all } g \in Q_8.$$

<1>2. Order computation for each element:
    *Proof:*
    <2>1. **Order 1:** The identity element $1$ is the unique element of order $1$ ($1^1 = 1$).
    <2>2. **Order of $-1$:** Since $-1 \neq 1$ and $(-1)^2 = 1$, the order of $-1$ is exactly $2$.
    <2>3. **Orders of $\pm i, \pm j, \pm k$:**
        - For $\pm i$: $(\pm i)^2 = i^2 = -1 \neq 1$, and $(\pm i)^4 = (-1)^2 = 1$, so $|\pm i| = 4$.
        - For $\pm j$: $(\pm j)^2 = j^2 = -1 \neq 1$, and $(\pm j)^4 = (-1)^2 = 1$, so $|\pm j| = 4$.
        - For $\pm k$: $(\pm k)^2 = k^2 = -1 \neq 1$, and $(\pm k)^4 = (-1)^2 = 1$, so $|\pm k| = 4$.

<1>3. Conclusion:
    The order distribution of the 8 elements of $Q_8$ is:
    - Order 1: $\{1\}$ (1 element),
    - Order 2: $\{-1\}$ (1 element),
    - Order 4: $\{i, -i, j, -j, k, -k\}$ (6 elements).
    Thus $-1$ is the unique element of order $2$ in $Q_8$. Q.E.D.
:::
