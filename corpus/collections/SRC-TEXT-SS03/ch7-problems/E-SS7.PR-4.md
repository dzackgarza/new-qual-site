---
schema: qual/card@1
id: E-SS7.PR-4
kind: problem
title: The prime number theorem in arithmetic progressions
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Prime Number Theorem
relations: []
review: draft
---

::: {.exercise}
$^*$ One can combine ideas from the prime number theorem with the proof of Dirichlet's theorem about primes in arithmetic progression (given in Book I) to prove the following. Let $q$ and $\ell$ be relatively prime integers. We consider the primes belonging to the arithmetic progression $\{qk + \ell\}_{k=1}^{\infty}$, and let $\pi_{q,\ell}(x)$ denote the number of such primes $\leq x$. Then one has
$$
\pi_{q,\ell}(x) \sim \frac{x}{\varphi(q)\log x} \quad \text{as } x \to \infty.
$$
:::

::: {.solution}
Let $q\ge2$, let $\ell$ be an integer coprime to $q$, and let $\varphi(q)$ be Euler's totient function. Let $\widehat G$ be the group of Dirichlet characters modulo $q$, with principal character $\chi_0$. For $\chi\in\widehat G$, put
$$
L(s,\chi)=\sum_{n=1}^\infty\chi(n)n^{-s},\qquad
\psi(x,\chi)=\sum_{n\le x}\chi(n)\Lambda(n),\qquad
\pi(x,\chi)=\sum_{p\le x}\chi(p).
$$
We reduce $\pi_{q,\ell}(x)$ to the character sums $\pi(x,\chi)$, evaluate the principal character by the prime number theorem, and evaluate the nonprincipal characters by the prime number theorem for Dirichlet $L$-functions.

::: pf

::: {.pf-step #orthogonality}
For every integer $n$ coprime to $q$,
$$
\frac{1}{\varphi(q)}\sum_{\chi\in\widehat G}\overline{\chi(\ell)}\chi(n)
=\begin{cases}1,&n\equiv\ell\pmod q,\\0,&n\not\equiv\ell\pmod q.\end{cases}
$$
Hence
$$
\pi_{q,\ell}(x)
=\frac{1}{\varphi(q)}\sum_{\chi\in\widehat G}\overline{\chi(\ell)}\sum_{\substack{p\le x\\p\nmid q}}\chi(p)
=\frac{1}{\varphi(q)}\sum_{\chi\in\widehat G}\overline{\chi(\ell)}\pi(x,\chi).
$$

::: pf-proof
The first identity is the orthogonality relation for the finite abelian group $(\ZZ/q\ZZ)^\times$. For $p\nmid q$, the inner sum in the second line is the indicator of $p\equiv\ell\pmod q$. For $p\mid q$, every character vanishes at $p$, and $p\not\equiv\ell\pmod q$, so these primes contribute nothing to either side. Hence the two sums agree exactly.
:::

:::

:::

::: pf

::: {.pf-step #principal}
The principal character satisfies
$$
\pi(x,\chi_0)=\pi(x)+O(1)\sim\frac{x}{\log x}.
$$

::: pf-proof
For $p\nmid q$, $\chi_0(p)=1$; for $p\mid q$, $\chi_0(p)=0$. The primes dividing $q$ are $O(1)$ in number, and the prime number theorem gives $\pi(x)\sim x/\log x$.
:::

:::

::: {.pf-step #nonprincipal}
Every nonprincipal character satisfies
$$
\pi(x,\chi)=o\left(\frac{x}{\log x}\right).
$$

::: pf-proof
First we prove $\psi(x,\chi)=o(x)$. The $L$-function $L(s,\chi)$ is entire because $\chi$ is nonprincipal. It does not vanish on the line $\Re s=1$. To see this, note that for $\sigma>1$,
$$
3\log\abs{L(\sigma,\chi_0)}+4\log\abs{L(\sigma+it,\chi)}+\log\abs{L(\sigma+2it,\chi^2)}\ge0,
$$
because the left side is the real part of
$$
\sum_{p\nmid q,m}\frac{1}{m}p^{-m\sigma}\left(3+4\chi(p)^mp^{-imt}+\chi(p)^{2m}p^{-2imt}\right),
$$
and $3+4\Re z+\Re z^2\ge0$ for $\abs{z}\le1$. If $L(1+it,\chi)=0$ for some $t\ne0$, then as $\sigma\to1^+$, the second term is $4\log(\sigma-1)+O(1)$, the first term is $-3\log(\sigma-1)+O(1)$, and the third term is bounded above, so the sum tends to $-\infty$, a contradiction. Hence $L(1+it,\chi)\ne0$. The same inequality, made quantitative, gives the standard zero-free region
$$
L(s,\chi)\ne0\quad\text{for}\quad \sigma>1-\frac{c}{\log(\abs{t}+2)}
$$
with a constant $c>0$, apart from a possible exceptional real zero $\beta<1$.

The explicit formula for $\psi(x,\chi)$ is
$$
\psi(x,\chi)=-\sum_{\abs{\Im\rho}\le T}\frac{x^\rho}{\rho}+O\left(\frac{x\log^2x}{T}\right)
$$
for $T\ge2$, where $\rho$ runs over the nontrivial zeros of $L(s,\chi)$. It follows from the Perron formula and the contour shift, exactly as in the proof of the prime number theorem; the only change is that $L(s,\chi)$ is entire, so there is no pole at $s=1$. Choose $T=\exp(c'\sqrt{\log x})$. The zero-free region gives
$$
\abs{\sum_{\abs{\Im\rho}\le T}\frac{x^\rho}{\rho}}
\le x^{1-c/\log T}\sum_{\abs{\Im\rho}\le T}\frac{1}{\abs{\rho}}
=O\left(xe^{-c''\sqrt{\log x}}\right)=o(x),
$$
and the exceptional real zero contributes $O(x^\beta)=o(x)$. The error term is $O(x\log^2x/T)=o(x)$. Hence $\psi(x,\chi)=o(x)$.

Partial summation gives
$$
\pi(x,\chi)=\frac{\psi(x,\chi)}{\log x}+\int_2^x\frac{\psi(t,\chi)}{t\log^2t}\,dt+O(x^{1/2}).
$$
The $O(x^{1/2})$ accounts for the prime powers $p^k$ with $k\ge2$. Since $\psi(t,\chi)=o(t)$, for every $\epsilon>0$ we have $\abs{\psi(t,\chi)}\le\epsilon t$ for all large $t$. Hence the first term is $o(x/\log x)$, the integral is $o(x/\log x)$, and $O(x^{1/2})=o(x/\log x)$. Therefore $\pi(x,\chi)=o(x/\log x)$.
:::

:::

:::

::: pf

::: {.pf-step #conclusion}
$$
\pi_{q,\ell}(x)\sim\frac{x}{\varphi(q)\log x}.
$$

::: pf-proof
By step [](#orthogonality){.pf-ref},
$$
\pi_{q,\ell}(x)=\frac{1}{\varphi(q)}\sum_{\chi\in\widehat G}\overline{\chi(\ell)}\pi(x,\chi).
$$
Step [](#principal){.pf-ref} gives $\pi(x,\chi_0)\sim x/\log x$, and step [](#nonprincipal){.pf-ref} gives $\pi(x,\chi)=o(x/\log x)$ for every $\chi\ne\chi_0$. Since $\widehat G$ has $\varphi(q)$ elements, which is fixed,
$$
\pi_{q,\ell}(x)
=\frac{1}{\varphi(q)}\left(\frac{x}{\log x}+o\left(\frac{x}{\log x}\right)\right)
\sim\frac{x}{\varphi(q)\log x}.
$$
:::

:::

:::

:::

