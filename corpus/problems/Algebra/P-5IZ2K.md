---
schema: qual/card@1
id: P-5IZ2K
kind: problem
title: A non-symmetric polynomial whose square is symmetric
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (asks
    for an example and its properties; both given, no repair needed), and the
    existing prose solution against a fresh re-derivation: x - y is not symmetric
    over a field of characteristic not 2, since swapping gives its negative and
    2(x - y) is nonzero, while its square is unchanged by the swap; the Vandermonde
    product is alternating, which the proof now derives rather than asserts — the
    ratio Delta^sigma/Delta is a sign, it is multiplicative because k[x] is a
    domain, it is -1 on a transposition by inspection of the single flipped factor,
    and being a homomorphism on a set of generators that agree with sign it equals
    sign; hence Delta^2 is symmetric and Delta is not, as 2 Delta is nonzero over a
    domain in characteristic not 2. Correct, and the characteristic-2 boundary is
    now stated explicitly rather than left to the reader: x - y = x + y is
    symmetric there, so no claim in that case is made. No source solution is
    retained for this card, so no source comparison was made. What was not checked:
    any printed source.
---

::: {.problem}
Find a non-symmetric polynomial in several variables whose square is symmetric, and prove its properties.
:::

::: {.solution}
Let $k$ be a field with $\operatorname{char}k\neq2$; for a polynomial $f\in k[x_1,\ldots,x_n]$ and $\sigma\in S_n$ write $f^\sigma$ for the polynomial obtained by substituting $x_{\sigma^{-1}(i)}$ for $x_i$, so that $f$ is symmetric when $f^\sigma=f$ for all $\sigma$ and alternating when $f^\sigma=\operatorname{sgn}(\sigma)f$.

::: pf

::: {.pf-step #example}
$P(x,y)=x-y$ is not symmetric, but $P^2$ is.

::: pf-proof
Swapping the two variables gives $(y-x)=-(x-y)$, which differs from $x-y$ because $2(x-y)\neq0$ in $k[x,y]$ when $\operatorname{char}k\neq2$. On the other hand $(y-x)^2=(x-y)^2$ in any commutative ring, so the square is unchanged by the only nontrivial permutation of the two variables, and it is therefore symmetric.
:::

:::

::: {.pf-step #vandermonde}
$\Delta=\prod_{i<j}(x_i-x_j)$ is alternating: $\Delta^\sigma=\operatorname{sgn}(\sigma)\Delta$ for every $\sigma\in S_n$.

::: pf-proof
For $\sigma\in S_n$ the product $\Delta^\sigma$ is $\prod_{i<j}(x_{\sigma(i)}-x_{\sigma(j)})$, which is a product of one factor $\pm(x_a-x_b)$ for each unordered pair $\{a,b\}$, so $\Delta^\sigma=\varepsilon(\sigma)\Delta$ with $\varepsilon(\sigma)\in\{\pm1\}$.

::: {.pf-step #homomorphism}
$\varepsilon\colon S_n\to\{\pm1\}$ is a homomorphism.

::: pf-proof
Applying $\tau$ and then $\sigma$ gives $(\Delta^\tau)^\sigma=\varepsilon(\sigma)\Delta^\tau=\varepsilon(\sigma)\varepsilon(\tau)\Delta$, while applying $\sigma\tau$ directly gives $\varepsilon(\sigma\tau)\Delta$; since $\Delta\neq0$ in the domain $k[x_1,\ldots,x_n]$, the two scalars agree.
:::

:::

::: {.pf-step #transposition}
$\varepsilon$ sends every transposition to $-1$.

::: pf-proof
For the transposition $\sigma=(12)$ every factor $x_i-x_j$ with $\{i,j\}\neq\{1,2\}$ is unchanged, and the single factor $x_1-x_2$ becomes $x_2-x_1=-(x_1-x_2)$; so $\Delta^\sigma=-\Delta$ and $\varepsilon(\sigma)=-1$. Any transposition is conjugate to $(12)$, and a homomorphism takes conjugate elements to conjugate elements, which in the abelian group $\{\pm1\}$ are equal; so $\varepsilon$ is $-1$ on every transposition.
:::

:::

Transpositions generate $S_n$, and $\operatorname{sgn}$ is the homomorphism $S_n\to\{\pm1\}$ sending each transposition to $-1$; two homomorphisms agreeing on a generating set agree everywhere, so $\varepsilon=\operatorname{sgn}$.
:::

:::

::: {.pf-step #square}
For $n\geq2$ the Vandermonde polynomial $\Delta$ is not symmetric, while $\Delta^2$ is.

::: pf-proof
A transposition $\tau$ is odd, so $\Delta^\tau=-\Delta\neq\Delta$ because $2\Delta\neq0$: the polynomial $\Delta$ is nonzero, being a product of nonzero factors, and $k[x_1,\ldots,x_n]$ has no zero divisors. Hence $\Delta$ is not symmetric. For any $\sigma$,
$$(\Delta^2)^\sigma=(\Delta^\sigma)^2=\operatorname{sgn}(\sigma)^2\Delta^2=\Delta^2,$$
since $\operatorname{sgn}(\sigma)=\pm1$; so $\Delta^2$ is symmetric.
:::

:::

::: {.pf-step}
There are non-symmetric polynomials with symmetric square: $x-y$ in two variables, and $\Delta$ in $n\geq2$ variables over any field of characteristic different from $2$.

::: pf-proof
The example $x-y$ is step [](#example){.pf-ref} and satisfies both properties. The Vandermonde polynomial does too by step [](#vandermonde){.pf-ref} and step [](#square){.pf-ref}, for every $n\geq2$. In characteristic $2$ the example degenerates — $x-y=x+y$ is then symmetric — which is why that hypothesis is stated; the question for characteristic $2$ is not answered here.
:::

:::

:::
:::
