---
schema: qual/card@1
id: P-BKS03-4A
kind: problem
title: Chebyshev polynomials with integer coefficients
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the substitution $q=e^{iz}$, the expansion of
    $(q+q^{-1})^{n}$, the recursion defining $T_{n}$, and the verification. The card's recursion was stated
    for all $n\ge0$ and then gives $T_{0}=0$, whereas the exercise needs $T_{0}=2$; the base case is now
    $T_{0}=2$ and the recursion runs from $n\ge1$, which is all the induction uses. No retained solution set
    covers this exercise, so the argument is the card's own.
---

::: {.problem}
Prove that for every integer $n\ge0$ there is a polynomial $T_n(x)\in\ZZ[x]$ such that
$$
2\cos(nz)=T_n(2\cos z)
$$
for every $z$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. The polynomials $T_{n}$ are built by induction, with $T_{0}=2$ and, for $n\ge1$, $T_{n}$ expressed through $T_{j}$ with $0<j<n$.

::: pf

::: {.pf-step #substitution}
Writing $q=e^{iz}$, the assertion $2\cos nz=T_{n}(2\cos z)$ becomes $q^{n}+q^{-n}=T_{n}(q+q^{-1})$.

::: pf-proof
$2\cos z=q+q^{-1}$ and $2\cos nz=q^{n}+q^{-n}$ by the definition of cosine in terms of exponentials, so substituting $2\cos z=q+q^{-1}$ on the right of the desired identity turns it into $q^{n}+q^{-n}=T_{n}(q+q^{-1})$. It is enough to produce, for each $n$, a polynomial in $\ZZ[x]$ with this property, since the substitution is reversible.
:::

:::

::: {.pf-step #expansion}
$(q+q^{-1})^{n}=q^{n}+q^{-n}+\sum\binom{n}{(n-j)/2}(q^{j}+q^{-j})+\delta$, the sum over $0<j<n$ with $n-j$ even, and $\delta=\binom{n}{n/2}$ if $n$ is even and $\delta=0$ if $n$ is odd.

::: pf-proof
Expand by the binomial theorem: $(q+q^{-1})^{n}=\sum_{k=0}^{n}\binom{n}{k}q^{n-2k}$. The terms with $k=0$ and $k=n$ give $q^{n}$ and $q^{-n}$. Every other $k$ pairs with $k'=n-k$, and the two terms are $\binom{n}{k}q^{j}$ and $\binom{n}{n-k}q^{-j}$ with $j=n-2k$, which are equal coefficients; the pair contributes $\binom{n}{k}(q^{j}+q^{-j})$ with $j=n-2k$ ranging over the integers strictly between $-n$ and $n$ congruent to $n$ mod $2$, and $k=(n-j)/2$. If $n$ is even, $k=n/2$ is left unpaired and contributes the constant $\binom{n}{n/2}$, and that is the $\delta$; if $n$ is odd no term is unpaired.
:::

:::

::: {.pf-step #recursion}
With $T_{0}=2$ and, for $n\ge1$,
$$
T_{n}(x)=x^{n}-\sum_{0<j<n,\ n-j\ \mathrm{even}}\binom{n}{(n-j)/2}T_{j}(x)-\begin{cases}\binom{n}{n/2},&n\text{ even},\\ 0,&n\text{ odd},\end{cases}
$$
the polynomial $T_{n}$ lies in $\ZZ[x]$ and has degree $n$.

::: pf-proof
Induction on $n$. For $n=0$ the polynomial $T_{0}=2$ is constant with integer coefficients. For $n\ge1$ the sum runs over positive $j<n$, so it involves only polynomials already constructed, all in $\ZZ[x]$ with degrees $j<n$; the binomial coefficients are integers; so $T_{n}\in\ZZ[x]$. Its leading term is $x^{n}$, because every subtracted term has degree at most $n-1$: the $T_{j}$ have degree $j\le n-1$, and the constants contribute nothing. Hence $\deg T_{n}=n$. Note that $j=0$ never occurs, so $T_{0}$ is not used by the recursion.
:::

:::

::: {.pf-step}
$2\cos nz=T_{n}(2\cos z)$ for every $n\ge0$.

::: pf-proof
For $n=0$ both sides are $2$, since $T_{0}=2$ and $\cos0=1$. For $n\ge1$, substitute $x=q+q^{-1}$ in the recursion of step [](#recursion){.pf-ref}: by the expansion of step [](#expansion){.pf-ref} the right-hand side becomes
$$
(q^{n}+q^{-n})+\sum\binom{n}{(n-j)/2}(q^{j}+q^{-j})+\delta-\sum\binom{n}{(n-j)/2}T_{j}(q+q^{-1})-\delta,
$$
and by the induction hypothesis $T_{j}(q+q^{-1})=q^{j}+q^{-j}$ for each $j$ in the sum, so the sum cancels against it term by term and the constants cancel too. What remains is $q^{n}+q^{-n}=2\cos nz$. So $T_{n}(2\cos z)=2\cos nz$ for every $z$ and every $n\ge0$, as required.
:::

:::

:::
:::
