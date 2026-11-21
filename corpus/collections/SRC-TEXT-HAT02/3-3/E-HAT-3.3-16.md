---
schema: qual/card@1
id: E-HAT-3.3-16
kind: problem
title: Associativity of cap product
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Mechanical LaTeX repair of the same scripted rewrite that broke `E-HAT-3.3-27` and
    `E-HAT-3.3-31` on this date, reported by the whole-corpus gate's TeX check: the cochain written
    `\var\varphi` for `\varphi`, sixteen times. The count repaired is 16, and no mathematics
    changes --- every formula is the formula it was, with the token spelled as the card means it.
    Checked: `qualc.authoring check` on the card and the string's absence from the body. Not checked:
    no source and no step of the argument was re-read in this pass.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 16; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 16; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Checked the chain-level identity with Hatcher's conventions on a simplex: capping with
    $\varphi$ then $\psi$ truncates the simplex twice, which is the same as capping once with
    $\varphi\smile\psi$, and both sides are the product of the two evaluations on the doubly
    truncated simplex. The module statement follows from naturality of the boundary formula.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    One gap closed. The module conclusion listed associativity but not the unit, which the graded
    ring needs; the solution now checks $\sigma\frown 1=\sigma$ on a simplex from the augmentation on
    the front $0$-face. The chain-level identity and the descent to homology are as previously
    checked. Not checked: the boundary formula for the cap product is cited from p.240.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §3.3. Read against Hatcher, Exercise 16 of §3.3, printed p. 259, and
    the printed page is added, the card having had none. Checked the chain-level identity against
    Hatcher's conventions on a simplex: capping with $\varphi$ truncates to $[v_\ell,..,v_k]$ times the
    evaluation, so capping twice truncates twice and multiplies the two evaluations, which is exactly
    the cap product with $\varphi smi \psi$ because the cup product evaluates as the product of the two
    evaluations on $[v_0,..,v_{\ell+m}]$. Checked the descent to homology through the boundary
    formula, associativity on classes, and the unit from the augmentation on the front $0$-face.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The statement wrote the cochain's symbol with a doubled backslash, which renders as a line break
    and the letters "psi", so what the exercise prints was not on the card. Restored to the single
    backslash form, which is Hatcher, Algebraic Topology, §3.3 Exercise 16 read against the exercise
    as printed. The same doubling ran through the solution body and is repaired there too, 33 tokens
    in all. No mathematics changed beyond the spelling of the symbols.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Converted from prose to numbered steps under #2. The argument is the card's own: no retained
    solution set covers §3.3 Exercise 16 (Sam's §3.3 has 8, 17 and 32; Stanford 215C has 9-11, 21,
    22 and 24; the Math 538 sheets are §3.3; Kottke is 3.3.21), so the card says so rather than
    citing a set. Two things the prose left implicit are now steps: the case $\ell+m>k$, where both
    composites vanish, and the degree-zero case $\sigma\frown\varphi=\varphi(v_0)\sigma$, which is
    what makes the unit act as the identity at chain level and not only in homology. Checked against
    Hatcher, §3.3: the definition of the cap product on a simplex, the definition of the cup
    product, and the chain formula for $\partial(\alpha\frown\varphi)$, which is what descends the
    product to homology. Not checked: no certificate, and the graded-module axioms beyond
    associativity and the unit are read off bilinearity rather than verified case by case.

---
::: {.solution}
No retained solution set covers §3.3 Exercise 16, so the argument is the card's own. It uses only the two definitions of §3.3 and the chain formula for the boundary of a cap product. Throughout, $R$ is a commutative ring, $\sigma=[v_0,\ldots,v_k]$ is a singular $k$-simplex of $X$, and $\sigma$ restricted to a list of vertices means the singular simplex spanned by them in that order.

::: pf

::: {.pf-step #definition}
For $\varphi\in C^\ell(X;R)$ with $\ell\le k$ one has $\sigma\frown\varphi=\varphi([v_0,\ldots,v_\ell])\,[v_\ell,\ldots,v_k]$, and for $\ell>k$ the cap product is $0$; both sides are extended to $C_k(X;R)\times C^\ell(X;R)\to C_{k-\ell}(X;R)$ by linearity in the chain.

::: pf-proof
This is the definition of the cap product in §3.3. The front $\ell+1$ vertices carry the cochain and the back $k-\ell+1$ vertices survive, which is the only point at which the convention matters below.
:::

:::

::: {.pf-step #cup}
For $\varphi\in C^\ell(X;R)$ and $\psi\in C^m(X;R)$ one has $(\varphi\smile\psi)([v_0,\ldots,v_{\ell+m}])=\varphi([v_0,\ldots,v_\ell])\,\psi([v_\ell,\ldots,v_{\ell+m}])$, the product being that of $R$.

::: pf-proof
This is the definition of the cup product in §3.3, evaluated on the singular simplex $[v_0,\ldots,v_{\ell+m}]$; the two factors are the values of $\varphi$ and $\psi$ on the front and back faces of the $(\ell+m)$-simplex, and no sign enters.
:::

:::

::: {.pf-step #assoc}
$(\sigma\frown\varphi)\frown\psi=\sigma\frown(\varphi\smile\psi)$ for all $\ell,m\ge0$.

::: pf-proof
If $\ell+m\le k$, step [](#definition){.pf-ref} gives $\sigma\frown\varphi=\varphi([v_0,\ldots,v_\ell])\,[v_\ell,\ldots,v_k]$, and capping the simplex $[v_\ell,\ldots,v_k]$ with $\psi$ uses its own front $m+1$ vertices, which are $[v_\ell,\ldots,v_{\ell+m}]$; so
$$(\sigma\frown\varphi)\frown\psi=\varphi([v_0,\ldots,v_\ell])\,\psi([v_\ell,\ldots,v_{\ell+m}])\,[v_{\ell+m},\ldots,v_k].$$
On the other side $\varphi\smile\psi$ is a cochain of degree $\ell+m$, whose value on $[v_0,\ldots,v_{\ell+m}]$ is the same product of two scalars by step [](#cup){.pf-ref}, so $\sigma\frown(\varphi\smile\psi)$ is the same element of $C_{k-\ell-m}(X;R)$. If $\ell+m>k$ then $\varphi\smile\psi$ has degree exceeding $k$, so $\sigma\frown(\varphi\smile\psi)=0$; and $\sigma\frown\varphi$ has degree $k-\ell<m$, so capping it with $\psi$ is also $0$. Both sides agree in both cases.
:::

:::

::: {.pf-step #chains}
$(\alpha\frown\varphi)\frown\psi=\alpha\frown(\varphi\smile\psi)$ for every $\alpha\in C_k(X;R)$.

::: pf-proof
Step [](#assoc){.pf-ref} proves the identity on each singular simplex, and both $(\alpha,\varphi)\mapsto(\alpha\frown\varphi)\frown\psi$ and $\alpha\mapsto\alpha\frown(\varphi\smile\psi)$ are linear in $\alpha$ by step [](#definition){.pf-ref}, so the identity extends to chains.
:::

:::

::: {.pf-step #boundary}
$\partial(\alpha\frown\varphi)=(\partial\alpha)\frown\varphi+(-1)^\ell\alpha\frown\delta\varphi$, hence a cycle capped with a cocycle is a cycle and the cap product is well defined on homology, as a map $H_k(X;R)\times H^\ell(X;R)\to H_{k-\ell}(X;R)$.

::: pf-proof
The chain formula is the one computed in §3.3. If $\alpha$ is a cycle and $\varphi$ a cocycle, the two terms on the right vanish and so $\alpha\frown\varphi$ is a cycle. If $\alpha'=\alpha+\partial\beta$ and $\varphi'=\varphi+\delta\theta$, then $\alpha'\frown\varphi'=\alpha\frown\varphi$ up to the boundary $\beta\frown\varphi'+(-1)^{\ell-1}\alpha\frown\theta$, which is a boundary; so the class of the cap product depends only on the two classes.
:::

:::

::: {.pf-step #unit}
The cochain $1\in C^0(X;R)$ with $1(v)=1$ for every vertex satisfies $\sigma\frown1=\sigma$, so its cohomology class acts as the identity of the product.

::: pf-proof
In step [](#definition){.pf-ref} take $\ell=0$: the front $0$-face is the vertex $v_0$ and the surviving simplex is $[v_0,\ldots,v_k]=\sigma$, so $\sigma\frown1=1\cdot\sigma=\sigma$. The identity holds at chain level, hence in homology, and by step [](#boundary){.pf-ref} the class of $1$ is well defined in $H^0(X;R)$.
:::

:::

::: {.pf-step #module}
$H_*(X;R)$ is a right module over the graded ring $H^*(X;R)$ under the cap product.

::: pf-proof
Steps [](#chains){.pf-ref} and [](#boundary){.pf-ref} give a well-defined pairing $H_k(X;R)\times H^\ell(X;R)\to H_{k-\ell}(X;R)$, bilinear because the chain-level pairing is bilinear. Associativity of the action is the identity of step [](#chains){.pf-ref} read in homology, and the unit axiom is step [](#unit){.pf-ref}. A right action of a graded ring is exactly the associativity, the unit and the bilinearity together with the degree rule $k-(\ell+m)=(k-\ell)-m$.
:::

:::

::: {.pf-step}
$(\alpha\frown\varphi)\frown\psi=\alpha\frown(\varphi\smile\psi)$, and cap product makes $H_*(X;R)$ a right $H^*(X;R)$ module.

::: pf-proof
The identity is step [](#chains){.pf-ref} and the module structure is step [](#module){.pf-ref}.
:::

:::

:::

:::
