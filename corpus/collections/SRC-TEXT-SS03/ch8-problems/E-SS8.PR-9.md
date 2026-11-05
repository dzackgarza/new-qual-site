---
schema: qual/card@1
id: E-SS8.PR-9
kind: problem
title: Arithmetic-geometric mean and Gauss's elliptic integral
classification:
  areas:
    - complex-analysis
  topics:
    - Elliptic Integrals
relations: []
review: draft
audit:
  - event: source-checked
    by: claude
    date: "2026-11-06"
    note: >-
      Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 8, §6, problem 9, read from the Zotero extraction of the book (attachment KGX4N6YF). The book defines $I(a,b)$ as the bare integral $\int_0^{\pi/2}d\theta/\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}$ and states Gauss's identity as $1/M(a,b)=\frac2\pi I(a,b)$; with that definition its printed relation $I(a,b)=\frac1aK(k)$ is correct. An earlier version of this card put $2/\pi$ inside $I$ and then reported the printed relation as an erratum; the statement and solution now use the book's normalization, and the erratum remark is deleted. Check at $a=b=1$: $I(1,1)=\pi/2=K(0)$ and $\frac2\pi I(1,1)=1=1/M(1,1)$.
  - event: solution-written
    by: claude
    date: 2026-11-01
    note: >-
      (a) monotonicity and $a_n-b_n\le(a-b)/2^n$, giving a common limit. (b) the Landen invariance is verified by the substitution $\sin\theta=\frac{2a\sin\varphi}{(a+b)+(a-b)\sin^2\varphi}$, with the derivative computed in full: it reduces to the identity $\bigl((a+b)-(a-b)s^2\bigr)^2=(a+b)^2-2(a^2-b^2)s^2+(a-b)^2s^4$; then continuity of $I$ gives $I(a,b)=I(M,M)=\pi/(2M)$. The relation $I(a,b)=K(k)/a$ follows from the substitution $x=\sin\theta$.
---

::: {.exercise}
Let $a_0=a\geq b=b_0>0$ and define
$$
a_{n+1}=\frac{a_n+b_n}{2},\qquad b_{n+1}=\sqrt{a_nb_n}.
$$

(a) Prove that $a_n$ and $b_n$ have a common limit $M(a,b)$, called the arithmetic-geometric mean.

(b) Gauss's identity states that
$$
\frac{1}{M(a,b)}=\frac2\pi\int_0^{\pi/2}
\frac{d\theta}{\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}}.
$$
Let $I(a,b)$ denote the integral on the right-hand side. Prove the identity by showing that it suffices to establish the invariance
$$
I(a,b)=I\left(\frac{a+b}{2},\sqrt{ab}\right).
$$
Also observe that
$$
I(a,b)=\frac1a K(k)=\frac1a\int_0^1
\frac{dx}{\sqrt{(1-x^2)(1-k^2x^2)}},
\qquad k^2=1-\frac{b^2}{a^2},
$$
and that the invariance follows from Chapter 8, Exercise 24(b).
:::

::: {.hint}
For (a), show $a_0\geq a_1\geq\cdots\geq a_n\geq b_n\geq\cdots\geq b_1\geq b_0$ and $a_n-b_n\leq(a-b)/2^n$.
:::

::: {.solution}

Let $a\ge b>0$ and $a_{n+1}=\frac{a_n+b_n}{2}$, $b_{n+1}=\sqrt{a_nb_n}$.

::: pf

::: {.pf-step #s1}

Part (a): $a=a_0\ge a_1\ge\cdots\ge a_n\ge b_n\ge\cdots\ge b_1\ge b_0=b$ and $a_n-b_n\le(a-b)/2^n$; hence $(a_n)$ and $(b_n)$ have a common limit $M(a,b)$.

::: pf-proof

By induction: if $a_n\ge b_n>0$ then
$$
b_n\le\sqrt{a_nb_n}=b_{n+1}\le a_{n+1}=\frac{a_n+b_n}{2}\le a_n,
$$
using the arithmetic–geometric mean inequality. So $(a_n)$ is nonincreasing and bounded below by $b$, $(b_n)$ is nondecreasing and bounded above by $a$; both converge, say $a_n\to A$, $b_n\to B$, and passing to the limit in $a_{n+1}=(a_n+b_n)/2$ gives $A=(A+B)/2$, that is $A=B$.

For the rate,
$$
a_{n+1}-b_{n+1}=\frac{a_n+b_n}{2}-\sqrt{a_nb_n}\le\frac{a_n+b_n}{2}-b_n=\frac{a_n-b_n}{2},
$$
so $a_n-b_n\le(a-b)/2^n\to0$.

:::

:::

::: {.pf-step #s2}

Part (b), the Landen invariance: $I(a,b)=I\!\left(\frac{a+b}{2},\sqrt{ab}\right)$.

::: pf-proof

Put $A=\frac{a+b}{2}$, $B=\sqrt{ab}$ and, for $0\le\varphi\le\frac\pi2$, let $\theta=\theta(\varphi)\in[0,\frac\pi2]$ be defined by
$$
\sin\theta=\frac{2a\sin\varphi}{(a+b)+(a-b)\sin^2\varphi} .
$$
The right side equals $0$ at $\varphi=0$ and $1$ at $\varphi=\frac\pi2$, and is continuous and strictly increasing, so $\theta$ runs from $0$ to $\frac\pi2$. Write $s=\sin\varphi$, $c=\cos\varphi$, $D=(a+b)+(a-b)s^2$ and $N=2as$. Then $\sin\theta=N/D$, and
$$
\cos\theta=\frac{\sqrt{D^2-N^2}}{D},\qquad
D^2-N^2=(1-s^2)\bigl((a+b)^2-(a-b)^2s^2\bigr),
$$
since $u=1$ is a root of the quadratic $(a+b)^2-2(a^2+b^2)u+(a-b)^2u^2$ in $u=s^2$.

Differentiating $\sin\theta=N/D$,
$$
\cos\theta\,\frac{d\theta}{d\varphi}=\frac{2ac\bigl((a+b)-(a-b)s^2\bigr)}{D^2}.
$$
Since $\cos\theta=c\sqrt{(a+b)^2-(a-b)^2s^2}/D$, this gives
$$
\frac{d\theta}{d\varphi}=\frac{2a\bigl((a+b)-(a-b)s^2\bigr)}{D\sqrt{(a+b)^2-(a-b)^2s^2}} .
$$
Also
$$
a^2\cos^2\theta+b^2\sin^2\theta=a^2-(a^2-b^2)\sin^2\theta
=\frac{a^2\bigl((a+b)^2-2(a^2-b^2)s^2+(a-b)^2s^4\bigr)}{D^2},
$$
and the bracket is $\bigl((a+b)-(a-b)s^2\bigr)^2$, so
$$
\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}=\frac{a\bigl((a+b)-(a-b)s^2\bigr)}{D} .
$$
Dividing,
$$
\frac{d\theta}{\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}}
=\frac{2\,d\varphi}{\sqrt{(a+b)^2-(a-b)^2\sin^2\varphi}}
=\frac{d\varphi}{\sqrt{A^2\cos^2\varphi+B^2\sin^2\varphi}},
$$
because $(a+b)^2-(a-b)^2s^2=4(A^2-B^2s^2)$ with $A^2-B^2=(a-b)^2/4$; explicitly $4A^2=4\cdot\frac{(a+b)^2}{4}=(a+b)^2$ and $4B^2=4ab$ give $A^2\cos^2\varphi+B^2\sin^2\varphi=\bigl((a+b)^2-(a-b)^2\sin^2\varphi\bigr)/4$. Integrating over $\varphi\in[0,\frac\pi2]$ gives $I(a,b)=I(A,B)$.

:::

:::

::: {.pf-step #s3}

Gauss's identity: $\dfrac{1}{M(a,b)}=\dfrac2\pi I(a,b)$.

::: pf-proof

By step [](#s2){.pf-ref} and induction, $I(a,b)=I(a_n,b_n)$ for every $n$. The function $I$ is continuous on the set $\{(x,y):x\ge y>0\}$ for the pairs arising here, since $a_n,b_n$ stay in the compact set $[b,a]$ with $b_n\ge b>0$ and the integrand is continuous and uniformly bounded there. Hence
$$
I(a,b)=\lim_{n\to\infty}I(a_n,b_n)=I(M,M),
$$
where $M=M(a,b)$ is the common limit of step [](#s1){.pf-ref}. At $a=b=M$ the integrand is the constant $1/M$, so
$$
I(M,M)=\int_0^{\pi/2}\frac{d\theta}{M}=\frac{\pi}{2M},
$$
and therefore $\frac2\pi I(a,b)=\frac2\pi\cdot\frac{\pi}{2M}=\frac1M$.

:::

:::

::: {.pf-step #s4}

The relation with the complete elliptic integral: $I(a,b)=\dfrac{1}{a}K(k)$ with $k^2=1-\dfrac{b^2}{a^2}$, where $K(k)=\displaystyle\int_0^1\frac{dx}{\sqrt{(1-x^2)(1-k^2x^2)}}$.

::: pf-proof

With $k^2=1-b^2/a^2$,
$$
a^2\cos^2\theta+b^2\sin^2\theta=a^2\bigl(1-k^2\sin^2\theta\bigr),
$$
so
$$
I(a,b)=\frac1a\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-k^2\sin^2\theta}} .
$$
Substituting $x=\sin\theta$ in that integral gives $\int_0^1dx/\sqrt{(1-x^2)(1-k^2x^2)}=K(k)$. Hence $I(a,b)=\frac{1}{a}K(k)$.

:::

:::

:::

:::
