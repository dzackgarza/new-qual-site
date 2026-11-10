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

(a) Show that the following three conditions are equivalent, in which case we say that $X$ is **geometrically irreducible**:

    - $\fiberprod{X}{k}{\bar{k}}$ is irreducible, where $\bar{k}$ denotes the algebraic closure of $k$;
    - $\fiberprod{X}{k}{k_s}$ is irreducible, where $k_s$ denotes the separable closure of $k$;
    - $\fiberprod{X}{k}{K}$ is irreducible for every extension field $K$ of $k$.

(b) Show that the following three conditions are equivalent, in which case we say $X$ is **geometrically reduced**:

    - $\fiberprod{X}{k}{\bar{k}}$ is reduced;
    - $\fiberprod{X}{k}{k_p}$ is reduced, where $k_p$ denotes the perfect closure of $k$;
    - $\fiberprod{X}{k}{K}$ is reduced for all extension fields $K$ of $k$.

(c) We say that $X$ is **geometrically integral** if $\fiberprod{X}{k}{\bar{k}}$ is integral.
Give examples of integral schemes which are neither geometrically irreducible nor geometrically reduced.
:::

::: {.solution}
Two standard results on base change for algebras of finite type over a field are used.

1. For a field $k$ and a $k$-algebra $R$, the following are equivalent: $\Spec(R\otimes_k K)$ is irreducible for every field extension $K/k$; $\Spec(R\otimes_k k_s)$ is irreducible; $\Spec(R\otimes_k \bar k)$ is irreducible. This is the Stacks Project, Lemma 10.47.3 (Tag 037K).
2. Let $S$ be a reduced $k$-algebra and $K/k$ a separable field extension. Then $K\otimes_k S$ is reduced. This is the Stacks Project, Lemma 10.43.6 (Tag 030U); over a perfect field every field extension is separable.

The step below records the two reductions that the proof of (1) uses, and the last step records that irreducibility of $R\otimes_k K$ cannot be tested by asking for $R\otimes_k K$ to be a domain.

::: pf

::: {.pf-step #xbark-irred-implies-xks-irred}
If $X_{\bar k}$ is irreducible, then $X_{k_s}$ is irreducible.

::: pf-proof
Choose an embedding
$$
k_s\subseteq\bar k.
$$
The projection
$$
X_{\bar k}\longrightarrow X_{k_s}
$$
is surjective because $\Spec\bar k\to\Spec k_s$ is faithfully flat and hence surjective, and surjectivity is preserved by base change.

The continuous image of an irreducible topological space is irreducible.  Hence irreducibility of $X_{\bar k}$ implies irreducibility of $X_{k_s}$.
:::

:::

::: {.pf-step #xks-irred-implies-xk-irred}
If $X_{k_s}$ is irreducible, then $X_K$ is irreducible for every extension field $K/k$.

::: pf-proof
Two inputs, both used on affine charts.

First, let $k''/k'$ be an algebraic purely inseparable extension.  Then $\Spec k''\to\Spec k'$ is surjective, integral and radical, hence a universal homeomorphism, so base change along it is a homeomorphism; in particular $X_{k''}\to X_{k'}$ is a homeomorphism.  Since every element of $\bar k$ separable over $k_s$ lies in $k_s$, the extension $\bar k/k_s$ is purely inseparable, so $X_{\bar k}\to X_{k_s}$ is a homeomorphism.

Second, let $k'$ be algebraically closed and let $Y$ be an irreducible scheme of finite type over $k'$.  Then $Y_\Omega$ is irreducible for every field extension $\Omega/k'$: on an affine chart $\Spec R$ of $Y$ the ring $R$ has a unique minimal prime, and extension of scalars over an algebraically closed field preserves the set of minimal primes (Stacks Project, Lemma 10.47.2).

Now let $K/k$ be arbitrary and choose a field $\Omega$ containing both $K$ and $\bar k$ over $k$.  By the hypothesis and the first input, $X_{\bar k}$ is irreducible; by the second input applied over the algebraically closed field $\bar k$, $X_\Omega=(X_{\bar k})_\Omega$ is irreducible.  The projection $X_\Omega\to X_K$ is surjective, because $\Spec\Omega\to\Spec K$ is faithfully flat, and the image of an irreducible space is irreducible.  Hence $X_K$ is irreducible.
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
$$
A\otimes_k k_p
\longrightarrow
A\otimes_k\bar k
$$
is injective because $k_p\to\bar k$ is an extension of fields and tensoring a $k_p$-vector space with $\bar k$ is faithful.

If $A\otimes_k k_p$ had a nonzero nilpotent, its image would be a nonzero nilpotent in $A\otimes_k\bar k$, contradiction.  Hence every affine chart of $X_{k_p}$ is reduced.
:::

:::

::: {.pf-step #xkp-reduced-implies-xk-reduced}
If $X_{k_p}$ is reduced, then $X_K$ is reduced for every extension field $K/k$.

::: pf-proof
The field $k_p$ is perfect, so every field extension of $k_p$ is separable.  By the second result of the preamble, applied over the perfect field $k_p$, a reduced algebra of finite type over $k_p$ stays reduced after every field extension: affinely, a reduced finitely generated algebra over a perfect field remains reduced after every field extension.  So $X_{k_p}$ reduced implies $(X_{k_p})_\Omega$ reduced for every extension $\Omega/k_p$.

Choose a common overfield $\Omega$ of $K$ and $k_p$.  The preceding fact gives that
$$
X_\Omega=(X_{k_p})_\Omega
$$
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
$$
k=\RR,
\qquad
X=\Spec\CC
$$
with its natural structure as an $\RR$-scheme.  Since $\CC$ is a field, $X$ is integral.

After base change to $\CC$,
$$
\CC\otimes_{\RR}\CC
\cong
\CC\times\CC.
$$
Thus
$$
X_\CC
\cong
\Spec\CC\amalg\Spec\CC
$$
is reducible.  Hence $X$ is not geometrically irreducible.
:::

:::

::: {.pf-step #integral-not-geom-reduced}
An integral scheme need not be geometrically reduced.

::: pf-proof
Let
$$
k=\FF_p(u)
$$
and set
$$
X=\Spec k[x]/(x^p-u).
$$
The element $u$ is not a $p$th power in $k$: its valuation at the prime $u$ is $1$, whereas a $p$th power has valuation divisible by $p$.  Hence
$$
x^p-u
$$
is irreducible over $k$, so the quotient is a field and $X$ is integral.

After adjoining $u^{1/p}$,
$$
x^p-u=(x-u^{1/p})^p.
$$
Therefore
$$
X_{k(u^{1/p})}
\cong
\Spec k(u^{1/p})[x]/(x-u^{1/p})^p
$$
is nonreduced.  Thus $X$ is not geometrically reduced.
:::

:::

::: {.pf-step #integral-neither-example}
There are integral schemes which are simultaneously neither geometrically irreducible nor geometrically reduced.

::: pf-proof
Let
$$
k=\FF_p(u,v),
$$
and let $w$ satisfy the Artin--Schreier equation
$$
w^p-w=v.
$$
This polynomial is separable because its derivative is $-1$.  It has no root in $k$: using the valuation at infinity in the variable $v$, normalized by
$$
\operatorname{ord}_\infty(v)=-1,
$$
one has
$$
\operatorname{ord}_\infty(r^p-r)
$$
either nonnegative, or a negative integer divisible by $p$, and therefore never $-1$.  An Artin--Schreier polynomial $T^p-T-v$ with no root is irreducible.  Thus
$$
L=k(w)
$$
is a finite separable extension of degree $p$.

Now put
$$
E=L(u^{1/p}),
\qquad
X=\Spec E.
$$
The element $u^{1/p}$ cannot lie in $L$: otherwise the nontrivial purely inseparable extension
$$
k(u^{1/p})/k
$$
would be a subextension of the separable extension $L/k$.  Hence
$$
[E:L]=p.
$$
Hence $E$ is a field and $X$ is integral.

Over an algebraic closure $\bar k$, the separable extension $L/k$ splits into $p$ distinct embeddings, while the purely inseparable equation becomes a $p$th power.  Consequently
$$
E\otimes_k\bar k
\cong
\prod_{j=1}^{p}
\bar k[\epsilon]/(\epsilon^p).
$$
This ring has more than one minimal prime and has nonzero nilpotents.  Therefore $X_{\bar k}$ is both reducible and nonreduced, so $X$ is neither geometrically irreducible nor geometrically reduced.
:::

:::

::: pf-qed
Step [](#irreducibility-tfae){.pf-ref} proves part (a), step [](#reducedness-tfae){.pf-ref} proves part (b), and steps [](#integral-not-geom-irreducible){.pf-ref}, [](#integral-not-geom-reduced){.pf-ref} and [](#integral-neither-example){.pf-ref} give the examples requested in part (c).
:::

:::

:::

::: {.remark}
Irreducibility of $X_K$ is weaker than reducedness, or domain-ness, of the corresponding ring.  Let $k$ be algebraically closed of characteristic $p>0$ and let
$$
A=k[x,y]/(y^p-x^p-x).
$$
Because $k$ is perfect, $k(x)^p=k(x^p)$, and $x^p+x\notin k(x^p)$ by comparing degrees in $x$; hence $y^p-x^p-x\in k(x)[y]$ is irreducible and $A$ is a domain.  Put $K=\Frac(A)=k(s)$ with $s^p=x^p+x$.  In $K[x,y]$ one has $y^p-x^p-x=(y-s)^p$, so
$$
A\otimes_k K\cong K[x,y]/((y-s)^p),
$$
in which $y-s$ is a nonzero nilpotent.  So a domain of finite type over an algebraically closed field can acquire nilpotents after a field extension, and irreducibility of $A\otimes_k K$ can be neither proved nor refuted by asking whether that ring is a domain.  What does survive is the number of minimal primes of $A\otimes_k K$, which is one here.
:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §3, Exercise 3.15, PDF pp. 26--27, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: for (a) Kim reduces a reducible $X_K$ to an affine chart with $A\otimes_kK$ reducible, extracts non-nilpotent $f_1,f_2$ with $f_1f_2=0$, and then asserts that the resulting finitely many polynomial conditions, which have a solution over the algebraically closed field $K$, have one over a finite extension of $k$; a finite purely inseparable base change of a separably closed $k$ is a homeomorphism, which would finish the argument.
That descent is asserted rather than proved, and it fails on the natural reading: a purely inseparable extension of a separably closed but non-perfect $k$ need not have a $k$-point, so a solution over $K$ does not specialize to one over $k$.
The proof above replaces it by the cited Lemma 10.47.3 and keeps Kim's two reductions, that purely inseparable base change is a homeomorphism and that extension of scalars over an algebraically closed field preserves the set of minimal primes.
Agree on the reduction, not on the descent step.  For (b) Kim uses the trace form of a Galois extension; the proof above uses the cited Lemma 10.43.6 over the perfect closure.
:::
