---
schema: qual/card@1
id: E-AMD-4WD576RU
kind: exercise
title: Show that if the minimal polynomial of a linear map $T$ is…
classification:
  areas:
  - algebra
  topics:
  - minimal-and-characteristic-polynomials
  - semisimplicity
  - linear-algebra
relations: []
review: draft
---

::: {.exercise}
Show that if the minimal polynomial of a linear operator $T: V \to V$ on a finite-dimensional vector space $V$ over a field $F$ is irreducible, then every $T\dash$invariant subspace has a $T\dash$invariant complement (i.e. $V$ is a semisimple $F[T]$-module).
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $V$ be a finite-dimensional vector space over a field $F$, and let $T \in \operatorname{End}_F(V)$.
We view $V$ as a module over the principal ideal domain (PID) $R = F[x]$, where the polynomial indeterminate $x$ acts as the linear transformation $T$ ($p(x) \cdot v = p(T)(v)$).

1. **Structure of the Module $V$ over $F[x]$:**
   Let $m_T(x) \in F[x]$ be the minimal polynomial of $T$.
   By assumption, $m_T(x) = p(x)$ is an irreducible polynomial in $F[x]$.
   Since $F[x]$ is a PID and $p(x)$ is irreducible, the ideal $\langle p(x) \rangle$ is a **maximal ideal**, and the quotient ring:
   $$
   K = F[x] / \langle p(x) \rangle
   $$
   is a **field** (an algebraic field extension of $F$ of degree $\deg p$).

2. **$V$ as a Vector Space over the Field $K$:**
   Since $m_T(T) = p(T) = 0$ on all of $V$, the annihilator of $V$ contains $\langle p(x) \rangle$.
   Therefore, the action of the ring $F[x]$ on $V$ factors through the quotient field $K = F[x]/\langle p(x) \rangle$:
   $$
   (f(x) + \langle p(x) \rangle) \cdot v := f(T)(v) \quad \text{for } f \in F[x], v \in V.
   $$
   This scalar multiplication is well-defined because if $f(x) - g(x) = q(x)p(x)$, then $(f(T) - g(T))(v) = q(T)p(T)(v) = 0$.
   Hence, $V$ is naturally a **vector space over the field $K$**.

3. **$T$-Invariant Subspaces and $K$-Subspaces:**
   A subspace $W \subseteq V$ is $T$-invariant if and only if $T(W) \subseteq W$, which is equivalent to $W$ being an $F[x]$-submodule of $V$.
   Since $V$ is a $K$-module and $K$ is a field, every $F[x]$-submodule of $V$ is precisely a **$K$-linear subspace** of $V$.

4. **Existence of $T$-Invariant Complement:**
   Let $W \subseteq V$ be a $T$-invariant subspace.
   Then $W$ is a $K$-linear subspace of the $K$-vector space $V$.
   By basic linear algebra over the field $K$ (choosing a $K$-basis for $W$ and extending it to a $K$-basis for $V$), every $K$-subspace $W$ has a $K$-linear complement $W'$:
   $$
   V = W \oplus W' \quad \text{as $K$-vector spaces}.
   $$
   Since $W'$ is a $K$-subspace, it is closed under the action of $K = F[x]/\langle p(x) \rangle$, and in particular $T(W') \subseteq W'$.
   Therefore, $W'$ is a $T$-invariant complement of $W$ in $V$.
:::
