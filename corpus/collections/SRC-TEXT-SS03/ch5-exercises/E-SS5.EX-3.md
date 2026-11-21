---
schema: qual/card@1
id: E-SS5.EX-3
kind: problem
title: The Jacobi theta function has order $2$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Theta Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 5 growth-order convention.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured both halves into numbered steps. Supplied the definition of order (the limsup of
    log log M(r) / log r) and the two estimates the upper bound needs: the elementary inequality
    2|n||y| <= (t/2)n^2 + (2/t)y^2, and the convergence of sum e^{-pi t n^2/2}, which turns the
    bound into C_t e^{(2 pi/t)|z|^2}. For the lower bound, supplied the justification for "not
    identically zero" (uniform convergence on the real interval makes termwise integration legal,
    and the n = 0 mode integrates to 1), and the argument that the points z_0 + m tau have
    |z_0 + m tau| = O(m) while log|Theta| grows like pi t m^2, which forces the limsup to be at
    least 2. Not checked this session: the printed statement page.

---

::: {.exercise}
Show that if $\tau$ is fixed with $\Im(\tau) > 0$, then the Jacobi theta function
$$
\Theta(z \thetaseparator \tau) = \sum_{n=-\infty}^{\infty} e^{\pi in^2\tau} e^{2\pi inz}
$$
is of order $2$ as a function of $z$. Further properties of $\Theta$ will be studied in Chapter 10.

[Hint: $-n^2 t + 2n\abs{z} \leq -n^2 t/2$ when $t > 0$ and $n \geq 4\abs{z}/t$.]
:::

::: {.solution}

The argument is the card's own; the statement is the exercise stored on the card, and no source text or solution set is retained for it.

Write $\tau=u+it$ with $t=\Im\tau>0$, and for an entire $f$ let $M(r)=\max_{\abs{z}\leq r}\abs{f(z)}$; the order of $f$ is $\rho=\limsup_{r\to\infty}\frac{\log\log M(r)}{\log r}$, with $\rho=2$ meaning that $\log M(r)\leq Cr^{2+\varepsilon}$ for every $\varepsilon>0$ and no smaller exponent works.

::: pf

::: {.pf-step #summand}
The series defining $\Theta(z\mid\tau)$ converges absolutely and uniformly on compact sets, and its $n$-th summand has modulus $e^{-\pi tn^{2}-2\pi ny}$ for $z=x+iy$.

::: pf-proof
$\abs{e^{\pi in^{2}\tau}e^{2\pi inz}}=e^{-\pi n^{2}t}\abs{e^{2\pi in(x+iy)}}=e^{-\pi tn^{2}}e^{-2\pi ny}$, and $\sum_{n}e^{-\pi tn^{2}}<\infty$ because $t>0$, so the series converges absolutely and uniformly in $z$ on any set where $y$ is bounded.
:::

:::

::: {.pf-step #inequality}
$2\abs{n}\abs{y}\leq\frac{t}{2}n^{2}+\frac{2}{t}y^{2}$.

::: pf-proof
$0\leq\bigl(\sqrt{t/2}\abs{n}-\sqrt{2/t}\abs{y}\bigr)^{2}=\frac{t}{2}n^{2}-2\abs{n}\abs{y}+\frac{2}{t}y^{2}$.
:::

:::

::: {.pf-step #upper}
$\abs{\Theta(z\mid\tau)}\leq C_{t}e^{(2\pi/t)\abs{z}^{2}}$.

::: pf-proof
By step [](#summand){.pf-ref}, $\abs{e^{\pi in^{2}\tau}e^{2\pi inz}}\leq e^{-\pi tn^{2}+2\pi\abs{n}\abs{y}}\leq e^{-\frac{\pi t}{2}n^{2}+\frac{2\pi}{t}y^{2}}$ using step [](#inequality){.pf-ref}. Summing, $\abs{\Theta(z\mid\tau)}\leq e^{2\pi y^{2}/t}\sum_{n}e^{-\pi tn^{2}/2}=C_{t}e^{2\pi y^{2}/t}$ with $C_{t}=\sum_{n}e^{-\pi tn^{2}/2}<\infty$. Since $y^{2}\leq\abs{z}^{2}$, this is at most $C_{t}e^{(2\pi/t)\abs{z}^{2}}$.
:::

:::

::: {.pf-step #order-at-most}
The order of $\Theta(\cdot\mid\tau)$ is at most $2$.

::: pf-proof
By step [](#upper){.pf-ref}, $\log M(r)\leq\log C_{t}+\frac{2\pi}{t}r^{2}\leq C'r^{2}$ for $r\geq1$, so $\log\log M(r)\leq\log C'+2\log r$ and $\frac{\log\log M(r)}{\log r}\leq2+o(1)$; hence $\rho\leq2$.
:::

:::

::: {.pf-step #quasi}
$\Theta(z+\tau\mid\tau)=e^{-\pi i\tau-2\pi iz}\Theta(z\mid\tau)$, and consequently $\Theta(z+m\tau\mid\tau)=e^{-\pi im^{2}\tau-2\pi imz}\Theta(z\mid\tau)$ for every integer $m\geq1$.

::: pf-proof
Reindexing the absolutely convergent series, whose terms are unchanged by a rearrangement,
$$
\Theta(z+\tau\mid\tau)=\sum_{n}e^{\pi in^{2}\tau}e^{2\pi in(z+\tau)}=\sum_{n}e^{\pi i(n^{2}+2n)\tau}e^{2\pi inz}.
$$
Putting $n=m-1$ and using $n^{2}+2n=(n+1)^{2}-1$ gives $e^{-\pi i\tau}\sum_{m}e^{\pi im^{2}\tau}e^{2\pi i(m-1)z}=e^{-\pi i\tau-2\pi iz}\Theta(z\mid\tau)$. For the second identity argue by induction on $m$: it holds for $m=1$, and if it holds for $m$ then applying the first identity with $w=z+m\tau$ gives
$$
\Theta(z+(m+1)\tau)=e^{-\pi i\tau-2\pi i(z+m\tau)}\,e^{-\pi im^{2}\tau-2\pi imz}\,\Theta(z)=e^{-\pi i(m+1)^{2}\tau-2\pi i(m+1)z}\Theta(z),
$$
since $1+2m+m^{2}=(m+1)^{2}$.
:::

:::

::: {.pf-step #nonzero}
$\Theta$ is not identically zero, and there is $z_{0}$ with $\Theta(z_{0}\mid\tau)\neq0$.

::: pf-proof
On the real interval $[0,1]$ the series converges uniformly by step [](#summand){.pf-ref}, so it may be integrated termwise: $\int_{0}^{1}\Theta(x\mid\tau)dx=\sum_{n}e^{\pi in^{2}\tau}\int_{0}^{1}e^{2\pi inx}dx$, and $\int_{0}^{1}e^{2\pi inx}dx$ is $1$ for $n=0$ and $0$ otherwise. Hence the integral is $1$, so $\Theta$ takes a nonzero value somewhere.
:::

:::

::: {.pf-step #lower}
The order of $\Theta(\cdot\mid\tau)$ is at least $2$.

::: pf-proof
Take $z_{0}$ as in step [](#nonzero){.pf-ref} and let $m\to\infty$. By step [](#quasi){.pf-ref},
$$
\log\abs{\Theta(z_{0}+m\tau\mid\tau)}=\log\abs{\Theta(z_{0}\mid\tau)}+\pi tm^{2}+2\pi m\Im z_{0},
$$
using $\abs{e^{-\pi im^{2}\tau}}=e^{\pi m^{2}t}$ and $\abs{e^{-2\pi imz_{0}}}=e^{2\pi m\Im z_{0}}$. Also $\abs{z_{0}+m\tau}\leq\abs{z_{0}}+m\abs{\tau}\leq Cm$ for $m\geq1$. Hence for $r_{m}=\abs{z_{0}+m\tau}$ we have $r_{m}\leq Cm$ while $\log M(r_{m})\geq\log\abs{\Theta(z_{0}+m\tau\mid\tau)}\geq cm^{2}\geq c'r_{m}^{2}$. Therefore $\log\log M(r_{m})\geq\log(c'r_{m}^{2})=2\log r_{m}+O(1)$, so the limsup defining the order is at least $2$.
:::

:::

::: {.pf-step}
$\rho_{\Theta}=2$.

::: pf-proof
Steps [](#order-at-most){.pf-ref} and [](#lower){.pf-ref} give $\rho\leq2$ and $\rho\geq2$.
:::

:::

:::

:::
