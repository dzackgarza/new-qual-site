---
schema: qual/card@1
id: E-6OUJV
kind: problem
title: Irreducible polynomials in characteristic $p$ are $g(x^{p^k})$ for unique separable
  $g$
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.exercise}
Let $k$ be a field with $\ch k = p>0$.
If $f\in k[x]^{\irr}$, then there is a unique separable $g\in k[x]^{\irr}$ such that $f(x) = g(x^{p^e})$ for some unique $e \ge 0$.
:::

::: {.solution}

No retained solution set covers this exercise: it is an unsorted compilation card with no book or sheet attributed in the collection `SRC-UNSORTED-ALGEBRA` (`source_kind: compilation`, date unknown), so the argument below is the card's own. It was read against the statements it uses — for an irreducible $g$ one has $g$ separable exactly when $g'\neq0$, and substitution $x\mapsto x^{p^{e}}$ is injective on $k[x]$ — and the uniqueness step is written out as a substitution rather than as the coefficient comparison the card's earlier prose asserted without argument.

Throughout, $k$ is a field with $\ch k=p>0$, $k[x]$ is the polynomial ring, $h'$ is the formal derivative, and a polynomial is separable when it has no repeated root in an algebraic closure of $k$.

::: pf

::: {.pf-step #derivative-criterion}
For $h=\sum_{i}a_{i}x^{i}\in k[x]$ one has $h'=0$ if and only if $h=h_{1}(x^{p})$ for some $h_{1}\in k[x]$.

:::: pf-proof

::: {.pf-step #coordinates}
$h'=0$ if and only if $a_{i}=0$ for every $i$ not divisible by $p$.

::: pf-proof
$h'=\sum_{i}i\,a_{i}x^{i-1}$, so $h'=0$ says $i\,a_{i}=0$ in $k$ for every $i$. In characteristic $p$ the integer $i$ is zero in $k$ exactly when $p\mid i$; so the condition is that $a_{i}=0$ for every $i$ with $p\nmid i$.
:::

:::

::: {.pf-step #substitution}
$h'=0$ if and only if $h=h_{1}(x^{p})$ for some $h_{1}$.

::: pf-proof
If $a_{i}=0$ whenever $p\nmid i$, then $h=\sum_{j}a_{jp}x^{jp}$, which is $h_{1}(x^{p})$ for $h_{1}(y)\coloneqq\sum_{j}a_{jp}y^{j}$. Conversely if $h=h_{1}(x^{p})$ then every exponent occurring in $h$ is divisible by $p$, so the coefficients indexed by the other exponents vanish.
:::

:::

::::

:::

::: {.pf-step #irreducible-substitution}
If $h\in k[x]$ is irreducible and $h=h_{1}(x^{p})$, then $h_{1}$ is irreducible.

::: pf-proof
A factorization $h_{1}=uv$ with both factors of positive degree would give $h=h_{1}(x^{p})=u(x^{p})v(x^{p})$, a factorization of $h$ into polynomials of positive degree, since $\deg u(x^{p})=p\deg u$ and likewise for $v$. So $h_{1}$ has no such factorization.
:::

:::

::: {.pf-step #existence}
There are $e\geq0$ and an irreducible $g\in k[x]$ with $f=g(x^{p^{e}})$, and $e$ is chosen maximal with this property.

:::: pf-proof

::: {.pf-step #admissible-set}
The set of $e\geq0$ for which $f=g(x^{p^{e}})$ for some $g\in k[x]$ is nonempty and bounded above.

::: pf-proof
$e=0$ is admissible with $g=f$. If $e$ is admissible, then $\deg f=p^{e}\deg g$ with $\deg g\geq1$, because $f$ is irreducible and hence nonconstant and $g$ is nonconstant as $f=g(x^{p^{e}})$ is; so $p^{e}\leq\deg f$ and $e\leq\log_{p}\deg f$. A nonempty set of natural numbers bounded above has a largest element.
:::

:::

::: {.pf-step #g-irreducible}
For the maximal $e$ and the corresponding $g$, the polynomial $g$ is irreducible.

::: pf-proof
$g$ has positive degree, and a factorization $g=g_{1}g_{2}$ with both factors of positive degree would give $f=g_{1}(x^{p^{e}})g_{2}(x^{p^{e}})$, contradicting the irreducibility of $f$.
:::

:::

::::

:::

::: {.pf-step #g-separable}
The polynomial $g$ of step [](#existence){.pf-ref} is separable, and $g'=0$ fails for it.

:::: pf-proof

::: {.pf-step #g-derivative-nonzero}
$g'\neq0$.

::: pf-proof
If $g'=0$, then $g=g_{1}(x^{p})$ by step [](#derivative-criterion){.pf-ref}, whence $f=g(x^{p^{e}})=g_{1}(x^{p^{e+1}})$, so $e+1$ would be admissible, contradicting the maximality of $e$.
:::

:::

::: {.pf-step #no-repeated-root}
$g$ has no repeated root.

::: pf-proof
Let $\alpha$ be a root of $g$ in an algebraic closure. If $\alpha$ were a multiple root, then $g$ and $g'$ would both vanish at $\alpha$, so $x-\alpha$ would divide both $g$ and $g'$ over that closure, and the minimal polynomial of $\alpha$ over $k$, which divides $g$ and is of positive degree, would have to equal $g$ up to a scalar by the irreducibility of $g$; hence $g$ would divide $g'$. But $g'\neq0$ by step [](#g-derivative-nonzero){.pf-ref} and $\deg g'<\deg g$ because $g$ is nonconstant, so $g$ cannot divide $g'$. Hence no root is multiple.
:::

:::

::::

:::

::: {.pf-step #unique-exponent}
The exponent $e$ of step [](#existence){.pf-ref} is unique among representations $f=h(x^{p^{j}})$ with $h$ separable.

:::: pf-proof

::: {.pf-step #equal-exponents}
If $f=g_{1}(x^{p^{e_{1}}})=g_{2}(x^{p^{e_{2}}})$ with $g_{1},g_{2}$ separable, then $e_{1}=e_{2}$.

::: pf-proof
Suppose $e_{1}<e_{2}$ and put $d\coloneqq e_{2}-e_{1}\geq1$. Substituting $y\coloneqq x^{p^{e_{1}}}$ in the identity $g_{1}(x^{p^{e_{1}}})=g_{2}(x^{p^{e_{2}}})=g_{2}\big((x^{p^{e_{1}}})^{p^{d}}\big)$ gives the identity $g_{1}(y)=g_{2}(y^{p^{d}})$ in $k[y]$. Every exponent occurring in $g_{2}(y^{p^{d}})$ is divisible by $p^{d}$, hence by $p$, so $g_{1}=h(y^{p})$ for a suitable $h$, and then $g_{1}'=0$ by step [](#derivative-criterion){.pf-ref}. But a separable polynomial of positive degree has nonzero derivative: if $g_{1}'=0$ then $g_{1}=h(y^{p})$ for some $h$, and over an algebraic closure of $k$, whose elements all have $p$-th roots, the identity $\big(\sum_{j}c_{j}^{1/p}y^{j}\big)^{p}=\sum_{j}c_{j}y^{jp}$ exhibits $g_{1}$ as the $p$-th power of a nonconstant polynomial, so every root of $g_{1}$ is a root of that polynomial as well and is therefore a multiple root, contrary to separability. This contradicts the separability of $g_{1}$, so $e_{1}<e_{2}$ is impossible; by symmetry $e_{2}<e_{1}$ is impossible too, and $e_{1}=e_{2}$.
:::

:::

::: {.pf-step #equal-polynomials}
If $f=g_{1}(x^{p^{e}})=g_{2}(x^{p^{e}})$ then $g_{1}=g_{2}$.

::: pf-proof
Substitution $x\mapsto x^{p^{e}}$ is injective on $k[x]$: if $u\neq v$ then $u-v$ is a nonzero polynomial of some degree $m\geq0$ and $(u-v)(x^{p^{e}})$ has degree $p^{e}m$, so it is nonzero as well. Applying this to $g_{1}-g_{2}$ and the common identity of the hypothesis gives $g_{1}-g_{2}=0$.
:::

:::

::::

:::

::: pf-step
Therefore there are a unique $e\geq0$ and a unique separable irreducible $g\in k[x]$ with $f(x)=g(x^{p^{e}})$.

::: pf-proof
Existence of such a pair is steps [](#existence){.pf-ref}, [](#g-irreducible){.pf-ref} and [](#g-separable){.pf-ref}; uniqueness of $e$ among all representations with separable $h$ is step [](#unique-exponent){.pf-ref}, and uniqueness of $g$ once $e$ is fixed is step [](#equal-polynomials){.pf-ref}. Hence the pair $(e,g)$ is unique.
:::

:::

:::

:::
