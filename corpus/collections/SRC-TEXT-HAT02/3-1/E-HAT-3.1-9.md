---
schema: qual/card@1
id: E-HAT-3.1-9
kind: problem
title: Hatcher Section 3.1 Exercise 9
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

# E-HAT-3.1-9

Show that if $f: S^n \to S^n$ has degree $d$ then $f^*: H^n(S^n; G) \to H^n(S^n; G)$ is multiplication by $d$.

::: {.solution}
<1>1. $H^n(S^n; G) \cong G$ and $H_n(S^n) \cong \ZZ$, with the natural pairing $H^n(S^n; G) \times H_n(S^n) \to G$ given by evaluation.
::: {.proof}
standard computation of the (co)homology of $S^n$.
:::

<1>2. Let $\alpha \in H^n(S^n; G)$ and $[S^n] \in H_n(S^n)$ the fundamental class.
::: {.proof}
choose a cohomology class and the fundamental class.
:::

<1>3. By naturality of the Kronecker pairing, $\langle f^*\alpha, [S^n] \rangle = \langle \alpha, f_*[S^n] \rangle$.
::: {.proof}
naturality of the evaluation pairing.
:::

<1>4. $f_*[S^n] = d[S^n]$ (by definition of degree).
::: {.proof}
the degree $d$ is defined by $f_*[S^n] = d[S^n]$.
:::

<1>5. Hence $\langle f^*\alpha, [S^n] \rangle = \langle \alpha, d[S^n] \rangle = d\langle \alpha, [S^n] \rangle$.
::: {.proof}
<1>3 and <1>4.
:::

<1>6. Since the pairing with $[S^n]$ identifies $H^n(S^n; G)$ with $G$ (it is an isomorphism), $f^*\alpha = d\alpha$.
::: {.proof}
<1>5 (the pairing $\alpha \mapsto \langle \alpha, [S^n] \rangle$ is an isomorphism $H^n(S^n;G) \to G$).
:::

<1>7. Hence $f^*$ is multiplication by $d$.
::: {.proof}
<1>6.
:::

<1>8. Q.E.D.
::: {.proof}
<1>7.
:::
:::
