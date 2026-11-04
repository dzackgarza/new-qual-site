---
schema: qual/card@1
id: E-SS7.EX-10
kind: problem
title: Asymptotic expansion of the logarithmic integral
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
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 7, §3, exercise 10, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, both parts and the hint; nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Both parts proved. (a) is one integration by parts together with the split of
    $\int_2^x dt/(\log t)^2$ at $\sqrt x$; the conclusion $\pi(x)\sim\operatorname{Li}(x)$ combines it
    with the prime number theorem $\pi(x)\sim x/\log x$ proved in Chapter 7, and it is cited, not
    reproved. (b) iterates the recursion
    $I_k=x/(\log x)^k+O(1)+k\,I_{k+1}$ for $I_k=\int_2^xdt/(\log t)^k$, and bounds
    $I_{N+1}=O(x/(\log x)^{N+1})$ by the same $\sqrt x$ split. Nothing is left in outline.
---

::: {.exercise}
In the theory of primes, define
$$
\operatorname{Li}(x)=\int_2^x\frac{dt}{\log t}.
$$

(a) Prove that $\operatorname{Li}(x)=x/\log x+O(x/(\log x)^2)$ as $x\to\infty$, and consequently that $\pi(x)\sim\operatorname{Li}(x)$.

(b) Show that for every integer $N>0$,
$$
\operatorname{Li}(x)=\sum_{k=1}^{N}\frac{(k-1)!x}{(\log x)^k}
+O\left(\frac{x}{(\log x)^{N+1}}\right)
\qquad(x\to\infty).
$$
:::

::: {.hint}
For (a), integrate by parts and split $\int_2^x dt/(\log t)^2$ at $\sqrt{x}$.
:::

::: {.solution}

Write $L=\log x$ and, for $k\ge1$,
$$
I_k(x)=\int_2^x\frac{dt}{(\log t)^k},
$$
so that $\operatorname{Li}(x)=I_1(x)$.

::: pf

::: {.pf-step #s1}

For every $k\ge1$,
$$
I_k(x)=\frac{x}{(\log x)^k}-\frac{2}{(\log 2)^k}+k\,I_{k+1}(x).
$$

::: pf-proof

Since $\dfrac{d}{dt}\dfrac{t}{(\log t)^k}=\dfrac{1}{(\log t)^k}-\dfrac{k}{(\log t)^{k+1}}$, integration by parts on $[2,x]$ gives
$$
I_k(x)=\Bigl[\frac{t}{(\log t)^k}\Bigr]_2^x+k\int_2^x\frac{dt}{(\log t)^{k+1}}=\frac{x}{(\log x)^k}-\frac{2}{(\log 2)^k}+k\,I_{k+1}(x).
$$

:::

:::

::: {.pf-step #s2}

For every $m\ge1$, $\;I_m(x)=O\bigl(x/(\log x)^m\bigr)$ as $x\to\infty$.

::: pf-proof

Split at $\sqrt x$. On $[2,\sqrt x]$ one has $\log t\ge\log2$, so
$$
\int_2^{\sqrt x}\frac{dt}{(\log t)^m}\le\frac{\sqrt x}{(\log 2)^m}=o\Bigl(\frac{x}{(\log x)^m}\Bigr).
$$
On $[\sqrt x,x]$ one has $\log t\ge\tfrac12\log x$, so
$$
\int_{\sqrt x}^{x}\frac{dt}{(\log t)^m}\le\frac{x-\sqrt x}{(\tfrac12\log x)^m}=\frac{2^m x}{(\log x)^m}\Bigl(1-o(1)\Bigr)=O\Bigl(\frac{x}{(\log x)^m}\Bigr).
$$
Adding the two gives the claim.

:::

:::

::: {.pf-step #s3}

Part (a): $\operatorname{Li}(x)=\dfrac{x}{\log x}+O\Bigl(\dfrac{x}{(\log x)^2}\Bigr)$ as $x\to\infty$.

::: pf-proof

Step [](#s1){.pf-ref} with $k=1$ gives $\operatorname{Li}(x)=I_1(x)=\dfrac{x}{\log x}-\dfrac{2}{\log 2}+I_2(x)$, and step [](#s2){.pf-ref} with $m=2$ gives $I_2(x)=O\bigl(x/(\log x)^2\bigr)$. The constant $2/\log2$ is absorbed in that $O$-term, so
$$
\operatorname{Li}(x)=\frac{x}{\log x}+O\Bigl(\frac{x}{(\log x)^2}\Bigr).
$$

:::

:::

::: {.pf-step #s4}

Consequently $\pi(x)\sim\operatorname{Li}(x)$.

::: pf-proof

The prime number theorem, $\pi(x)\sim x/\log x$ as $x\to\infty$ (Chapter 7), together with step [](#s3){.pf-ref} which gives $\operatorname{Li}(x)\sim x/\log x$, yields
$$
\frac{\pi(x)}{\operatorname{Li}(x)}=\frac{\pi(x)}{x/\log x}\cdot\frac{x/\log x}{\operatorname{Li}(x)}\longrightarrow1\cdot1=1 .
$$

:::

:::

::: {.pf-step #s5}

Part (b): for every integer $N>0$,
$$
\operatorname{Li}(x)=\sum_{k=1}^{N}\frac{(k-1)!\,x}{(\log x)^k}+O\Bigl(\frac{x}{(\log x)^{N+1}}\Bigr).
$$

::: pf-proof

Iterating step [](#s1){.pf-ref}, and writing $c_k=2/(\log 2)^k$, induction on $N$ gives
$$
I_1(x)=\sum_{k=1}^{N}(k-1)!\,\frac{x}{(\log x)^k}-D_N+N!\,I_{N+1}(x),
\qquad D_N=\sum_{k=1}^{N}(k-1)!\,c_k .
$$
Indeed, for $N=1$ this is exactly $I_1=x/\log x-c_1+I_2$, and if it holds for $N$ then substituting $I_{N+1}=x/(\log x)^{N+1}-c_{N+1}+(N+1)I_{N+2}$ turns the remainder into $N!\,x/(\log x)^{N+1}$, which is the $k=N+1$ term since $N!=((N+1)-1)!$, and leaves $-(D_N+N!\,c_{N+1})=-D_{N+1}$ together with $(N+1)!\,I_{N+2}$.

By step [](#s2){.pf-ref} with $m=N+1$, $\;N!\,I_{N+1}(x)=O\bigl(x/(\log x)^{N+1}\bigr)$, and the constant $-D_N$ is absorbed in the same $O$-term. Hence
$$
\operatorname{Li}(x)=I_1(x)=\sum_{k=1}^{N}\frac{(k-1)!\,x}{(\log x)^k}+O\Bigl(\frac{x}{(\log x)^{N+1}}\Bigr).
$$

:::

:::

:::

:::
