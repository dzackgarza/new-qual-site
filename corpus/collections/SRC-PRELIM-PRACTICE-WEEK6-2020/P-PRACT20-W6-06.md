---
schema: qual/card@1
id: P-PRACT20-W6-06
kind: problem
title: Separating continuity, uniform continuity, Lipschitz continuity and differentiability on $(-1,1)$
classification:
  areas:
  - prelim
  topics:
  - Uniform Continuity
  - Lipschitz Continuity
  - Differentiability
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-PRACTICE-WEEK6-2020 has an empty provenance list, and the only
    retained pages of the practice sheet are the three page images
    assets/attachments/prelim-practice-week6-2020/page-4.png, page-5.png and
    page-11.png, none of which carries this problem; so there is no printed page
    to compare the statement with. What was checked is the statement as it stands
    on the card: the four requests were matched to four explicit functions, and each asserted property was verified, including the failure modes
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. Four explicit examples, with the failure of uniform continuity, of the Lipschitz condition, of differentiability at 0, and of continuity of the derivative, each verified
---

::: {.problem}
Find examples of a function $f : ( - 1 , 1 ) \to \RR$ which is

(A) continuous but not uniformly continuous,

(B) uniformly continuous but not Lipschitz continuous,

(C) Lipschitz continuous but not differentiable,

(D) differentiable but not continuously differentiable.
:::

::: {.solution}

All four examples live on $(-1,1)$; the properties are verified where the exam
asks for an example, and each function is real-valued on that interval.

::: pf

::: {.pf-step #continuousnotuniform}

(A) $f(x)=\dfrac{1}{1-\abs x}$ is continuous but not uniformly continuous on
$(-1,1)$.

::: pf-proof

The function is continuous on $(-1,1)$, since $1-\abs x>0$ there. It is not
uniformly continuous: the points $x_n=1-1/n$ and $y_n=1-2/n$ satisfy
$\abs{x_n-y_n}=1/n\to0$ while $f(x_n)=n$ and $f(y_n)=n/2$, so
$\abs{f(x_n)-f(y_n)}=n/2$ is unbounded; a uniformly continuous function cannot
send pairs at distance tending to $0$ to pairs at distance bounded below.

:::

:::

::: {.pf-step #uniformnotlipschitz}

(B) $f(x)=\sqrt{\abs x}$ is uniformly continuous but not Lipschitz on
$(-1,1)$.

::: pf-proof

$\sqrt{\abs\cdot}$ is continuous on the compact interval $[-1,1]$, hence
uniformly continuous there, and the restriction to $(-1,1)$ inherits uniform
continuity. It is not Lipschitz: at points $x>0$ and $0$, $\frac{\abs{\sqrt
x-0}}{\abs{x-0}}=x^{-1/2}\to\infty$ as $x\to0^{+}$, so no constant $C$
satisfies $\abs{f(x)-f(0)}\le C\abs x$ for all $x\in(-1,1)$.

:::

:::

::: {.pf-step #lipschitznotdifferentiable}

(C) $f(x)=\abs x$ is Lipschitz but not differentiable on $(-1,1)$.

::: pf-proof

$\abs{\abs a-\abs b}\le\abs{a-b}$ by the triangle inequality, so $f$ is
Lipschitz with constant $1$. At $0$ the difference quotients are $\frac{\abs
h}{h}$, which is $1$ for $h>0$ and $-1$ for $h<0$, so the two one-sided limits
differ and $f$ is not differentiable at $0$.

:::

:::

::: {.pf-step #differentiablenotc1}

(D) $f(x)=x^2\sin(1/x)$ for $x\ne0$ and $f(0)=0$ is differentiable on $(-1,1)$
but not continuously differentiable there.

::: pf-proof

Off $0$ the function is a product of differentiable functions, with
$f'(x)=2x\sin(1/x)-\cos(1/x)$. At $0$,
$\left|\frac{f(h)-f(0)}{h}\right|=\abs{h\sin(1/h)}\le\abs h\to0$, so $f'(0)=0$
exists. But $f'(x)$ has no limit at $0$: along $x_n=1/(2\pi n)$ it equals
$2x_n\sin(2\pi n)-\cos(2\pi n)=-1$, while $f'(0)=0$, so $f'$ is not continuous
at $0$.

:::

:::

:::


:::
