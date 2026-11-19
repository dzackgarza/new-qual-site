---
schema: qual/card@1
id: P-BKS03-6B
kind: problem
title: Elements of equal finite order in $\operatorname{PGL}_2(\CC)$ are conjugate up to a power
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the argument into numbered steps, and repaired a directional error in its last
    sentence. The transcription concluded that b is conjugate to a power of a, whereas the exercise
    asks for c with c a c^{-1} a power of b; the two are different statements, and the proof now
    finishes in the direction asked, using that the exponent k with zeta' = zeta^k is coprime to n,
    so some l has kl congruent to 1 modulo n and a = (a^k)^l is conjugate to (b)^l. Also supplied the
    steps the prose compressed: A^n = lambda I for a representing a, the rescaling to A^n = I,
    diagonalizability from the distinct roots of x^n - 1, and the argument that the order of A
    equals n because A^m being scalar forces it to be the identity. Every macro used is one the
    preamble defines. No source text is retained for this examination.

---

::: {.problem}
Let $a,b\in\operatorname{PGL}_2(\CC)$ have the same finite order $n$.
Prove that there exists $c\in\operatorname{PGL}_2(\CC)$ such that $cac^{-1}$ is a power of $b$.
:::

::: {.solution}

The argument is the card's own; the card is an examination problem and no published solution is retained for it. It is stated for $\operatorname{PGL}_{2}(\CC)=\operatorname{GL}_{2}(\CC)/\CC^{\times}$.

::: pf

::: {.pf-step #scalar}
If $A\in\operatorname{GL}_{2}(\CC)$ represents the class $a$ of finite order $n$, then $A^{n}=\lambda I$ for some $\lambda\neq0$, and after rescaling $A$ by a scalar one may assume $A^{n}=I$.

::: pf-proof
$a^{n}=1$ in the quotient means $A^{n}$ lies in the kernel $\CC^{\times}$, that is $A^{n}=\lambda I$ with $\lambda\neq0$; the representatives of $a$ are exactly the nonzero scalar multiples of $A$, and rescaling does not change the class. Choose $\mu$ with $\mu^{n}=\lambda$, which exists since $\CC$ is algebraically closed and $\lambda\neq0$; then $(A/\mu)^{n}=A^{n}/\mu^{n}=\lambda I/\lambda=I$, and $A/\mu$ still represents $a$.
:::

:::

::: {.pf-step #diagonalisable}
A matrix $A$ with $A^{n}=I$ is diagonalisable, and its eigenvalues are $n$-th roots of unity.

::: pf-proof
The polynomial $x^{n}-1$ has derivative $nx^{n-1}$, whose only root is $0$, and $0^{n}-1=-1\neq0$, so $x^{n}-1$ has no repeated root (characteristic $0$); a matrix annihilated by a polynomial with distinct roots is diagonalisable. Its eigenvalues $\lambda$ satisfy $\lambda^{n}=1$ because $A^{n}=I$.
:::

:::

::: {.pf-step #normal-form}
After conjugating and rescaling, $A=\begin{pmatrix}1&0\\ 0&\zeta\end{pmatrix}$ where $\zeta$ is an $n$-th root of unity, and $\zeta$ is primitive.

::: pf-proof
By step [](#diagonalisable){.pf-ref} $A$ is conjugate to $\operatorname{diag}(\alpha,\beta)$ with $\alpha^{n}=\beta^{n}=1$; at least one of them is nonzero, both are, and rescaling by $\alpha^{-1}$ gives $\operatorname{diag}(1,\beta/\alpha)$ with $\beta/\alpha$ an $n$-th root of unity. Write $\zeta=\beta/\alpha$. If $A^{m}=sI$ for some $m\geq1$ and scalar $s$, comparing upper left entries gives $s=1$. Now $a^{m}=1$ in the quotient exactly when $A^{m}$ is scalar, hence exactly when $A^{m}=I$; so the least $m$ with $a^{m}=1$, which is $n$, is also the least $m$ with $A^{m}=I$, which is the order of $\zeta$ (the order of $\operatorname{diag}(1,\zeta)$ is the order of $\zeta$ because the first entry is $1$). So $\zeta$ is a primitive $n$-th root of unity.
:::

:::

::: {.pf-step #b-normal}
Likewise $b$ is represented by a matrix conjugate to $B=\begin{pmatrix}1&0\\ 0&\zeta'\end{pmatrix}$ with $\zeta'$ a primitive $n$-th root of unity.

::: pf-proof
The preceding three steps use only that $b$ has order $n$, which is the hypothesis.
:::

:::

::: {.pf-step #power}
There is $k$ with $\gcd(k,n)=1$ and $\zeta'=\zeta^{k}$, hence $B=A^{k}$.

::: pf-proof
The primitive $n$-th roots of unity are exactly $\zeta^{k}$ with $\gcd(k,n)=1$, since they are the elements of order $n$ in the cyclic group of $n$-th roots of unity; and $\operatorname{diag}(1,\zeta)^{k}=\operatorname{diag}(1,\zeta^{k})=B$.
:::

:::

::: {.pf-step #direction}
There is $c$ with $cac^{-1}=b^{l}$ for some $l$, namely $l$ with $kl\equiv1\pmod n$.

::: pf-proof
By steps [](#normal-form){.pf-ref}, [](#b-normal){.pf-ref} and [](#power){.pf-ref} there are $g,h\in\operatorname{GL}_{2}(\CC)$ with $A=g^{-1}\cdot\operatorname{diag}(1,\zeta)\cdot g$ and $B=h^{-1}\operatorname{diag}(1,\zeta^{k})h$, and $\operatorname{diag}(1,\zeta^{k})=A^{k}$; so $b$ is represented by a conjugate of $a^{k}$, say $b=\bar m\,a^{k}\bar m^{-1}$ in the quotient. Choose $l$ with $kl\equiv1\pmod n$, possible because $\gcd(k,n)=1$. Then, since $a^{n}=1$,
$$
a=a^{kl}=(a^{k})^{l}=\bigl(\bar m^{-1}b\,\bar m\bigr)^{l}=\bar m^{-1}b^{l}\,\bar m,
$$
so with $c=\bar m$ we get $cac^{-1}=b^{l}$. (For $n=1$ both classes are trivial and any $c$ works.)
:::

:::

:::

:::
