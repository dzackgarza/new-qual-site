---
schema: qual/card@1
id: E-SS7.EX-11
kind: problem
title: Equivalent forms of the prime number theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Prime Number Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 7, §3, exercise 11, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise (the print writes $\phi$ where the card writes $\varphi$); nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    All four implications proved in the cycle (i)$\Rightarrow$(ii)$\Rightarrow$(i),
    (i)$\Leftrightarrow$(iii), (iii)$\Leftrightarrow$(iv). The only tool is partial summation, stated
    and proved once, plus the bound $\varphi(y)\le y\log y$ and the book's Proposition 2.2 for
    (iv)$\Rightarrow$(iii); the converse (iii)$\Rightarrow$(iv) is an $\varepsilon$-argument on
    $\psi_1(x)=\int_1^x\psi$. Nothing is left in outline.
---

::: {.exercise}
Let $\varphi(x)=\sum_{p\leq x}\log p$, where the sum runs over primes. Prove that the following assertions are equivalent as $x\to\infty$:

(i) $\varphi(x)\sim x$;

(ii) $\pi(x)\sim x/\log x$;

(iii) $\psi(x)\sim x$;

(iv) $\psi_1(x)\sim x^2/2$.
:::

::: {.solution}

Recall $\varphi(x)=\sum_{p\le x}\log p$, $\pi(x)=\sum_{p\le x}1$, $\psi(x)=\sum_{p^k\le x}\log p$ and $\psi_1(x)=\int_1^x\psi(u)\,du$. Throughout, $\varphi(y)\le(\log y)\,\pi(y)\le y\log y$ for $y\ge2$.

::: pf

::: {.pf-step #s1}

Partial summation. If $(a_p)$ is a sequence indexed by the primes and $A(x)=\sum_{p\le x}a_p$, then for $f\in C^1$ and $x\ge2$,
$$
\sum_{p\le x}a_pf(p)=A(x)f(x)-\int_2^xA(t)f'(t)\,dt .
$$

::: pf-proof

$A$ is a step function on $[2,x]$, constant between consecutive primes. Since $\int_p^xf'(t)dt=f(x)-f(p)$ and $A(t)=A(p)$ for $t$ from $p$ to the next prime,
$$
\int_2^xA(t)f'(t)\,dt=\sum_{p\le x}a_p\int_p^xf'(t)\,dt=\sum_{p\le x}a_p\bigl(f(x)-f(p)\bigr)=A(x)f(x)-\sum_{p\le x}a_pf(p).
$$

:::

:::

::: {.pf-step #s2}

(i)$\;\Rightarrow\;$(ii).

::: pf-proof

Take $a_p=1$, so $A=\pi$, and $f(t)=1/\log t$, so $f'(t)=-1/(t(\log t)^2)$. By step [](#s1){.pf-ref},
$$
\pi(x)=\frac{\varphi(x)}{\log x}+\int_2^x\frac{\varphi(t)}{t(\log t)^2}\,dt .
$$
If $\varphi(t)=t(1+o(1))$, the first term is $x/\log x\,(1+o(1))$, and the integral is at most $2\int_2^xdt/(\log t)^2=O(x/(\log x)^2)=o(x/\log x)$ for large $x$ by the split at $\sqrt x$. Hence $\pi(x)\sim x/\log x$.

:::

:::

::: {.pf-step #s3}

(ii)$\;\Rightarrow\;$(i).

::: pf-proof

Take $a_p=1$ and $f(t)=\log t$, so $f'=1/t$. By step [](#s1){.pf-ref},
$$
\varphi(x)=\pi(x)\log x-\int_2^x\frac{\pi(t)}{t}\,dt .
$$
If $\pi(t)=t/\log t\,(1+o(1))$, the first term is $x(1+o(1))$, while the integral is at most $\int_2^x\bigl(1+o(1)\bigr)dt/\log t\sim\operatorname{Li}(x)=o(x)$, because $\operatorname{Li}(x)=x/\log x+O(x/(\log x)^2)$. So $\varphi(x)/x\to1$.

:::

:::

::: {.pf-step #s4}

(i)$\;\Leftrightarrow\;$(iii).

::: pf-proof

Every prime power $p^k\le x$ with $k\ge1$ contributes $\log p$, so
$$
\psi(x)=\sum_{k\ge1}\varphi\bigl(x^{1/k}\bigr),
$$
a finite sum ($\varphi(x^{1/k})=0$ once $x^{1/k}<2$).

If $\varphi(x)\sim x$: the $k=1$ term is $\varphi(x)$ and each $k\ge2$ term is at most $x^{1/k}\log x\le x^{1/2}\log x$, with at most $\log_2x$ terms, so the whole tail is $O(x^{1/2}(\log x)^2)=o(x)$; hence $\psi(x)=\varphi(x)+o(x)\sim x$.

If $\psi(x)\sim x$: since $\psi\ge\varphi$ one has $\limsup\varphi(x)/x\le1$, and $\psi(x)\le\varphi(x)+O(x^{1/2}(\log x)^2)$ by the same estimate, so $\varphi(x)/x\ge\psi(x)/x-o(1)\to1$; hence $\varphi(x)\sim x$.

:::

:::

::: {.pf-step #s5}

(iii)$\;\Leftrightarrow\;$(iv).

::: pf-proof

(iv)$\Rightarrow$(iii) is Proposition 2.2 of Chapter 7: $\psi_1(x)\sim x^2/2$ implies $\psi(x)\sim x$.

(iii)$\Rightarrow$(iv): let $\varepsilon>0$ and choose $X$ with $\abs{\psi(u)-u}\le\varepsilon u$ for $u\ge X$. Then for $x\ge X$,
$$
\psi_1(x)=\int_1^X\psi(u)\,du+\int_X^x\psi(u)\,du=C+\frac{x^2-X^2}{2}+O(\varepsilon x^2)
$$
with $C$ a constant, so
$$
\frac{\psi_1(x)}{x^2/2}=1+\frac{2C-X^2}{x^2}+O(\varepsilon)\longrightarrow1+O(\varepsilon),
$$
and letting $\varepsilon\to0$ gives $\psi_1(x)\sim x^2/2$.

:::

:::

::: {.pf-step #s6}

All four assertions are equivalent.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give (i)$\Leftrightarrow$(ii); step [](#s4){.pf-ref} gives (i)$\Leftrightarrow$(iii); step [](#s5){.pf-ref} gives (iii)$\Leftrightarrow$(iv). Composing, any two of (i)--(iv) imply each other, so the four assertions are equivalent as $x\to\infty$.

:::

:::

:::

:::
