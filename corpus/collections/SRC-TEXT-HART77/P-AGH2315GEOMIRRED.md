---
schema: qual/card@1
id: P-AGH2315GEOMIRRED
kind: problem
title: Geometric irreducibility, reducedness, and integrality after base change
classification:
  areas:
  - algebraic-geometry
  topics:
  - Base Change
  - Irreducibility
  - Reduced Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.15 statement and the standard separable-closure/perfect-closure tests for geometric irreducibility and reducedness.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a scheme of finite type over a field $k$, not necessarily algebraically closed.
Here $\fiberprod{X}{k}{K}$ abbreviates $\fiberprod{X}{\Spec k}{\Spec K}$.

a. Show that the following three conditions are equivalent, in which case we say that $X$ is **geometrically irreducible**:

    - $\fiberprod{X}{k}{\bar{k}}$ is irreducible, where $\bar{k}$ denotes the algebraic closure of $k$;
    - $\fiberprod{X}{k}{k_s}$ is irreducible, where $k_s$ denotes the separable closure of $k$;
    - $\fiberprod{X}{k}{K}$ is irreducible for every extension field $K$ of $k$.

b. Show that the following three conditions are equivalent, in which case we say $X$ is **geometrically reduced**:

    - $\fiberprod{X}{k}{\bar{k}}$ is reduced;
    - $\fiberprod{X}{k}{k_p}$ is reduced, where $k_p$ denotes the perfect closure of $k$;
    - $\fiberprod{X}{k}{K}$ is reduced for all extension fields $K$ of $k$.

c. We say that $X$ is **geometrically integral** if $\fiberprod{X}{k}{\bar{k}}$ is integral.
Give examples of integral schemes which are neither geometrically irreducible nor geometrically reduced.
:::

::: {.solution}
We use two standard field-extension facts for finite-type schemes:

1. geometric irreducibility can be tested after base change to a separable algebraic closure;
2. geometric reducedness can be tested after base change to the perfect closure.

These are the scheme forms of Stacks Project, Lemmas 33.8.9 and 33.6.4, respectively.

::: pf

::: {.pf-step #xbark-irred-implies-xks-irred}
If $X_{\bar k}$ is irreducible, then $X_{k_s}$ is irreducible.

::: pf-proof
Choose an embedding
\[
k_s\subseteq\bar k.
\]
The projection
\[
X_{\bar k}\longrightarrow X_{k_s}
\]
is surjective because $\Spec\bar k\to\Spec k_s$ is faithfully flat and hence surjective, and surjectivity is preserved by base change.

The continuous image of an irreducible topological space is irreducible.  Hence irreducibility of $X_{\bar k}$ implies irreducibility of $X_{k_s}$.
:::

:::

::: {.pf-step #xks-irred-implies-xk-irred}
If $X_{k_s}$ is irreducible, then $X_K$ is irreducible for every extension field $K/k$.

::: pf-proof
This is the standard separable-closure criterion for geometric irreducibility.  The algebraic content is the following pair of facts.

First, over a separably closed field, an irreducible scheme remains irreducible after every field extension: affinely, tensoring a ring with a unique minimal prime over a separably closed field with a field extension again has a unique minimal prime.

Second, given $K/k$ there is a common overfield $\Omega$ containing both $K$ and $k_s$ over $k$.  The first fact gives that
\[
X_\Omega=(X_{k_s})_\Omega
\]
is irreducible.  The projection
\[
X_\Omega\longrightarrow X_K
\]
is surjective, so $X_K$ is irreducible.

This is precisely the implication in the separable-closure test for geometric irreducibility.
:::

:::

::: {.pf-step #irreducibility-tfae}
The following are equivalent:

1. $X_{\bar k}$ is irreducible;
2. $X_{k_s}$ is irreducible;
3. $X_K$ is irreducible for every field extension $K/k$.

::: pf-proof
Step [](#xbark-irred-implies-xks-irred){.pf-ref} proves $(1)\Rightarrow(2)$, and step [](#xks-irred-implies-xk-irred){.pf-ref} proves $(2)\Rightarrow(3)$.  The implication $(3)\Rightarrow(1)$ is immediate by taking $K=\bar k$.
:::

:::

::: {.pf-step #xbark-reduced-implies-xkp-reduced}
If $X_{\bar k}$ is reduced, then $X_{k_p}$ is reduced.

::: pf-proof
Embed the perfect closure $k_p$ into $\bar k$.  On an affine open $U=\Spec A\subseteq X$, the ring map
\[
A\otimes_k k_p
\longrightarrow
A\otimes_k\bar k
\]
is injective because $k_p\to\bar k$ is an extension of fields and tensoring a $k_p$-vector space with $\bar k$ is faithful.

If $A\otimes_k k_p$ had a nonzero nilpotent, its image would be a nonzero nilpotent in $A\otimes_k\bar k$, contradiction.  Hence every affine chart of $X_{k_p}$ is reduced.
:::

:::

::: {.pf-step #xkp-reduced-implies-xk-reduced}
If $X_{k_p}$ is reduced, then $X_K$ is reduced for every extension field $K/k$.

::: pf-proof
The field $k_p$ is perfect.  A reduced finite-type scheme over a perfect field is geometrically reduced: affinely, a reduced finitely generated algebra over a perfect field remains reduced after every field extension.

Choose a common overfield $\Omega$ of $K$ and $k_p$.  The preceding fact gives that
\[
X_\Omega=(X_{k_p})_\Omega
\]
is reduced.

On every affine chart of $X_K$, the base-change map to the corresponding affine chart of $X_\Omega$ is injective because $K\to\Omega$ is a field extension.  A nilpotent in the source would therefore give a nilpotent in the reduced target.  Hence $X_K$ is reduced.

Equivalently, this is the perfect-closure criterion for geometric reducedness: finite purely inseparable extensions are exactly the obstruction, and they all embed in $k_p$.
:::

:::

::: {.pf-step #reducedness-tfae}
The following are equivalent:

1. $X_{\bar k}$ is reduced;
2. $X_{k_p}$ is reduced;
3. $X_K$ is reduced for every field extension $K/k$.

::: pf-proof
Step [](#xbark-reduced-implies-xkp-reduced){.pf-ref} proves $(1)\Rightarrow(2)$, and step [](#xkp-reduced-implies-xk-reduced){.pf-ref} proves $(2)\Rightarrow(3)$.  The implication $(3)\Rightarrow(1)$ is immediate by taking $K=\bar k$.
:::

:::

::: {.pf-step #integral-not-geom-irreducible}
An integral scheme need not be geometrically irreducible.

::: pf-proof
Take
\[
k=\mathbb R,
\qquad
X=\Spec\mathbb C
\]
with its natural structure as an $\mathbb R$-scheme.  Since $\mathbb C$ is a field, $X$ is integral.

After base change to $\mathbb C$,
\[
\mathbb C\otimes_{\mathbb R}\mathbb C
\cong
\mathbb C\times\mathbb C.
\]
Thus
\[
X_\mathbb C
\cong
\Spec\mathbb C\amalg\Spec\mathbb C
\]
is reducible.  Hence $X$ is not geometrically irreducible.
:::

:::

::: {.pf-step #integral-not-geom-reduced}
An integral scheme need not be geometrically reduced.

::: pf-proof
Let
\[
k=\mathbb F_p(u)
\]
and set
\[
X=\Spec k[x]/(x^p-u).
\]
The element $u$ is not a $p$th power in $k$: its valuation at the prime $u$ is $1$, whereas a $p$th power has valuation divisible by $p$.  Hence
\[
x^p-u
\]
is irreducible over $k$, so the quotient is a field and $X$ is integral.

After adjoining $u^{1/p}$,
\[
x^p-u=(x-u^{1/p})^p.
\]
Therefore
\[
X_{k(u^{1/p})}
\cong
\Spec k(u^{1/p})[x]/(x-u^{1/p})^p
\]
is nonreduced.  Thus $X$ is not geometrically reduced.
:::

:::

::: {.pf-step #integral-neither-example}
There are integral schemes which are simultaneously neither geometrically irreducible nor geometrically reduced.

::: pf-proof
Let
\[
k=\mathbb F_p(u,v),
\]
and let $w$ satisfy the Artin--Schreier equation
\[
w^p-w=v.
\]
This polynomial is separable because its derivative is $-1$.  It has no root in $k$: using the valuation at infinity in the variable $v$, normalized by
\[
\operatorname{ord}_\infty(v)=-1,
\]
one has
\[
\operatorname{ord}_\infty(r^p-r)
\]
either nonnegative, or a negative integer divisible by $p$, and therefore never $-1$.  An Artin--Schreier polynomial $T^p-T-v$ with no root is irreducible.  Thus
\[
L=k(w)
\]
is a finite separable extension of degree $p$.

Now put
\[
E=L(u^{1/p}),
\qquad
X=\Spec E.
\]
The element $u^{1/p}$ cannot lie in $L$: otherwise the nontrivial purely inseparable extension
\[
k(u^{1/p})/k
\]
would be a subextension of the separable extension $L/k$.  Hence
\[
[E:L]=p.
\]
Hence $E$ is a field and $X$ is integral.

Over an algebraic closure $\bar k$, the separable extension $L/k$ splits into $p$ distinct embeddings, while the purely inseparable equation becomes a $p$th power.  Consequently
\[
E\otimes_k\bar k
\cong
\prod_{j=1}^{p}
\bar k[\epsilon]/(\epsilon^p).
\]
This ring has more than one minimal prime and has nonzero nilpotents.  Therefore $X_{\bar k}$ is both reducible and nonreduced, so $X$ is neither geometrically irreducible nor geometrically reduced.
:::

:::

::: pf-qed
Step [](#irreducibility-tfae){.pf-ref} proves part (a), step [](#reducedness-tfae){.pf-ref} proves part (b), and steps [](#integral-not-geom-irreducible){.pf-ref}, [](#integral-not-geom-reduced){.pf-ref} and [](#integral-neither-example){.pf-ref} give the examples requested in part (c).
:::

:::

:::
