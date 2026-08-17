---
schema: qual/card@1
id: P-5CQNK
kind: problem
title: Positive derivative of monotone functions, and measurability of $f^{-1}(E)\cap\{f'>0\}$
classification:
  areas:
  - real-analysis
  topics:
  - absolute-continuity
  - differentiation
  - measure-theory
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Determine whether the following statements are true and false.
If true, provide a proof.
If false, prove a counter example.

a. If $f(x)$ is a increasing, continuous function on the interval $[0,1]$ such that $f(0)=0$ and $f(1)=1$, then there exists a set $E \subset [0,1]$ of positive measure such that $f'(x) > 0$.
b. If $f(x)$ is a strictly increasing, absolutely continuous function on the interval $[0,1]$ with $f(0)=0$ and $f(1)=1$, then the set $f^{-1}(E) \cap \{x \in [0,1] : f'(x) > 0\}$ is measurable for any measurable set $E \subset [0,1]$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. (a) is FALSE. Proof: take the Cantor function $c$: it is increasing, continuous, $c(0)=0$, $c(1)=1$, and $c'(x) = 0$ for a.e. $x\in[0,1]$ (the derivative is $0$ on the complement of the Cantor set, which has measure zero).
Hence $\{x : c'(x) > 0\}$ has measure zero, so no positive-measure set $E$ with $f' > 0$ on $E$ exists.
<1>2. (b) is TRUE. Proof: since $f$ is strictly increasing and continuous on $[0,1]$, it is a homeomorphism onto $[0,1]$ (as $f(0)=0$, $f(1)=1$); let $g = f^{-1}$.
Write the measurable set $E$ as $E = B \cup N$ with $B$ Borel and $N$ Lebesgue-null.
Then $f^{-1}(E) = g(E) = g(B) \cup g(N)$.
<1>3. $g(B)$ is Borel.
Proof: $g$ is continuous (the inverse of a strictly increasing continuous function on a compact interval is continuous), and $g$ is hence Borel measurable; so $g(B)$ is a Borel set.
<1>4. $g(N)$ is null.
Proof: it suffices to show $m(g(N)) = 0$.
Since $f$ is absolutely continuous and strictly increasing, the change-of-variables formula holds: for every non-negative measurable $h$, \[ \int_0^1 h(f(x))\,f'(x)\,dx = \int_0^1 h(t)\,dt, \] (as $f$ AC implies $f'$ exists a.e., $f' \ge 0$, and the formula $\int h(f)f' = \int h$ holds).
Applying this to $h = \chi_N$: \[ m(N) = 0 = \int_0^1 \chi_N(t)\,dt = \int_0^1 \chi_N(f(x))\,f'(x)\,dx = \int_{f^{-1}(N)} f'(x)\,dx . \] Hence $f' = 0$ a.e. on $f^{-1}(N) = g(N)$ (since $f' \ge 0$). But $f' > 0$ a.e. on $\{x : f'(x) > 0\}$ by definition, so $m\big(g(N) \cap \{f' > 0\}\big) = 0$.
(Alternative: $f$ AC has the Luzin $N$-property — it maps null sets to null sets — and the change-of-variables argument above is the direct proof for the inverse.)
In particular $g(N)$ need not itself be null, but its intersection with $\{f' > 0\}$ is null.
<1>5. $f^{-1}(E) \cap \{x : f'(x) > 0\}$ is measurable.
Proof: $\{f' > 0\}$ is measurable ($f$ AC $\Rightarrow$ $f'$ exists a.e. and is measurable; extend arbitrarily off the differentiability set).
By <1>2--<1>4, \[ f^{-1}(E) \cap \{f' > 0\} = \big(g(B) \cap \{f'>0\}\big) \cup \big(g(N) \cap \{f'>0\}\big), \] the union of a Borel set (<1>3) and a null set (<1>4), hence measurable.
<1>6. Q.E.D.
:::
