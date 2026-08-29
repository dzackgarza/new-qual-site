---
schema: qual/card@1
id: P-KHZD3
kind: problem
title: Whether a formal power series ring is a UFD
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Rings
  - Local Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Is a ring of formal power series $R[[x]]$ a unique factorization domain (UFD)?
:::

::: solution
**Goal:** Determine whether $R[[x]]$ is a UFD when $R$ is a field, a PID, or a general UFD, and discuss multivariate power series $R[[x_1, \dots, x_n]]$.

<1>1. Case 1: $R = k$ is a field:
    *Proof:*
    <2>1. If $k$ is a field, $k[[x]]$ is a discrete valuation ring (DVR) and a principal ideal domain (PID).
    <2>2. Every non-zero element $f(x) \in k[[x]]$ can be uniquely written as $f(x) = x^n u(x)$ where $n \ge 0$ is the order $\operatorname{ord}(f)$ and $u(x) \in k[[x]]^\times$ is a unit (since its constant term is non-zero).
    <2>3. Up to associates, the only irreducible element is $x$.
    <2>4. Every PID is a UFD, so $k[[x]]$ is a UFD.

<1>2. Case 2: $R$ is a PID:
    *Proof:*
    <2>1. If $R$ is a PID (or a regular local ring), then $R[[x]]$ is a UFD.
    <2>2. For example, $\mathbb{Z}[[x]]$ is a UFD.

<1>3. Case 3: $R$ is a general UFD (Pierre Samuel's 1961 Counterexample):
    *Proof:*
    <2>1. Unlike the polynomial case ($R \text{ UFD} \implies R[x] \text{ UFD}$ by Gauss's Lemma), $R[[x]]$ **need not be a UFD** even when $R$ is a UFD!
    <2>2. **Counterexample (Samuel, 1961):** Let $k$ be a field of characteristic $\ne 2$. Consider the ring:
        $$R = \frac{k[X, Y, Z]}{(X^2 + Y^3 + Z^7)}.$$
        Samuel proved that $R$ is a UFD (in fact, a 2-dimensional normal domain), but the formal power series ring $R[[T]]$ is **not** a UFD.

<1>4. Multivariate case over a field:
    *Proof:*
    <2>1. (Auslander–Buchsbaum Theorem, 1959): Every regular local ring is a UFD.
    <2>2. For any field $k$, the ring $k[[x_1, \dots, x_n]]$ is a regular local ring of dimension $n$, hence a UFD for all $n \ge 1$.

<1>5. Conclusion:
    $R[[x]]$ is a UFD if $R$ is a field or a PID (or regular local ring), but in general $R$ being a UFD does not imply $R[[x]]$ is a UFD (Samuel's counterexample). Over a field $k$, $k[[x_1, \dots, x_n]]$ is always a UFD by Auslander-Buchsbaum. Q.E.D.
:::
