---
schema: qual/card@1
id: E-SSA.PR-4
kind: problem
title: Coefficients of a generating function with poles on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Generating Functions
  - Asymptotics
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 4,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Solution installed: the residue formula on |w| = rho with rho > 1 gives F_n as minus the sum of the residues of F w^{-n-1} plus O(rho^{-n}), and each residue is a_j^{-n} times a polynomial of degree r_j - 1 by the book's Theorem 1.4 and Leibniz. Checked on F = 1/((w-1)^2 (w+1)).
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the solution installed on 2026-11-01, whose mathematics is transcribed rather than
    re-derived. The five numbered paragraphs become steps, and the two corrections to the printed statement become
    a step of their own, so the card cannot be read as proving the statement as printed: the minus sign in front of
    the residue and the factor alpha_j^{-n} are both carried, with the counterexample F(w) = 1/(w-i) for the
    second. The three checks keep their own step. Recomputed here: the residue at w=1 of F w^{-n-1} for
    F = 1/(w-1) is 1 while F_n = -1, so the sign is genuinely part of the statement; and for
    F = 1/((w-1)^2(w+1)) the partial fractions give F_n = n/2 + 3/4 + (-1)^n/4, matching the two P_j. Not checked:
    the book's own text of the problem beyond the card's OCR transcription of PDF pages 359-363; the statement is
    unchanged here. No statement repair beyond the two corrections the card already documents.
---

::: {.exercise}
Suppose $F(z)=\sum_{n=0}^{\infty}F_nw^n$ is meromorphic in a region containing the closed unit disc, and the only poles of $F$ are on the unit circle at the points $\alpha_1,\dots,\alpha_k$, and their orders are $r_1,\dots,r_k$ respectively. Then for some $\epsilon>0$
$$
F_n=\sum_{j=1}^{k}P_j(n)+O(e^{-\epsilon n})\qquad\text{as } n\to\infty,
$$
where each $P_j$ is a polynomial of degree $r_j-1$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's provenance is the book, quoted through the OCR transcription of its Appendix A Problems, and the argument on the card is its own. **Two corrections to the printed statement are part of the card**, and the proof below establishes the corrected form: the sum $\sum_jP_j(n)$ carries a **minus** sign in front of each residue, and each $P_j$ is $\alpha_j^{-n}$ times a polynomial in $n$ rather than a polynomial in $n$ (which is the same thing only when every pole is at $1$). Write $\DD=\{\abs w<1\}$, let $\Omega\supset\overline\DD$ be a region on which $F$ is meromorphic with poles exactly the distinct $\alpha_1,\dots,\alpha_k\in\partial\DD$ of orders $r_1,\dots,r_k$, and write $F(w)=\sum_{n\ge0}F_nw^n$.

::: pf

::: {.pf-step #disc}
There is $\rho>1$ such that $\overline{D_\rho}\subset\Omega$ and $F$ is holomorphic on $D_\rho\setminus\{\alpha_1,\dots,\alpha_k\}$.

::: pf-proof
$\overline\DD$ is compact and lies in the open set $\Omega$, so $\delta_0=\operatorname{dist}(\overline\DD,\CC\setminus\Omega)>0$; put $\rho=1+\delta_0/2>1$, so that $\overline{D_\rho}\subset\Omega$. The poles of $F$ in $\Omega$ are exactly the $\alpha_j$, all of modulus $1$, so $F$ is holomorphic on $D_\rho$ off those points.
:::

:::

::: {.pf-step #residue}
For $n\ge0$, with $H_n(w)=F(w)w^{-n-1}$ and $M=\sup_{\abs w=\rho}\abs F<\infty$,
$$
F_n=\sum_{j=1}^{k}P_j(n)+O(\rho^{-n}),\qquad P_j(n):=-\operatorname{res}_{\alpha_j}H_n .
\tag{2}
$$

::: pf-proof
On $D_\rho$ the function $H_n$ is holomorphic except for a pole of order $n+1$ at $0$ and a pole of order $r_j$ at each $\alpha_j$, since $w^{-n-1}$ is holomorphic and nonzero there. The residue formula on the circle $\abs w=\rho$ gives $\frac{1}{2\pi i}\oint_{\abs w=\rho}H_n=\operatorname{res}_0H_n+\sum_j\operatorname{res}_{\alpha_j}H_n$, and $\operatorname{res}_0H_n=F_n$ because the coefficient of $w^{-1}$ in $F(w)w^{-n-1}$ is the coefficient of $w^n$ in $F$. On the circle $F$ is continuous, so the integral is at most $\frac{1}{2\pi}\cdot2\pi\rho\cdot M\rho^{-n-1}=M\rho^{-n}$. Rearranging gives (2), the minus sign being absorbed into the definition of $P_j$.
:::

:::

::: {.pf-step #formula}
$P_j(n)=-\dfrac{1}{(r_j-1)!}\Bigl(\dfrac{d}{dw}\Bigr)^{r_j-1}\Bigl[(w-\alpha_j)^{r_j}F(w)w^{-n-1}\Bigr]_{w=\alpha_j}$.

::: pf-proof
This is the formula for the residue at a pole of order $r$, applied to $H_n$ at $\alpha_j$ and multiplied by the $-1$ in the definition of $P_j$; it is the formula displayed in the problem, with the sign correction.
:::

:::

::: {.pf-step #polynomial}
$P_j(n)=\alpha_j^{-n}Q_j(n)$ with $Q_j$ of degree $r_j-1$ and leading coefficient $A_j=\dfrac{(-1)^{r_j}G_j(\alpha_j)}{(r_j-1)!}\alpha_j^{-r_j}\ne0$, where $G_j(w)=(w-\alpha_j)^{r_j}F(w)$.

::: pf-proof
$G_j$ is holomorphic near $\alpha_j$ with $G_j(\alpha_j)\ne0$ because the pole has order exactly $r_j$. Leibniz applied to the preceding formula gives a sum over $i=0,\dots,r_j-1$ of $\frac{G_j^{(i)}(\alpha_j)}{i!(r_j-1-i)!}$ times $\bigl(\frac{d}{dw}\bigr)^{r_j-1-i}w^{-n-1}$ at $\alpha_j$, and $\bigl(\frac{d}{dw}\bigr)^{s}w^{-n-1}=(-1)^s(n+1)\cdots(n+s)w^{-n-1-s}$. As $\abs{\alpha_j}=1$, each summand is $\alpha_j^{-n}$ times a polynomial in $n$ of degree $r_j-1-i$, so $P_j=\alpha_j^{-n}Q_j$ with $\deg Q_j\le r_j-1$; the term $i=0$ has degree exactly $r_j-1$ with coefficient $\frac{(-1)^{r_j}G_j(\alpha_j)}{(r_j-1)!}\alpha_j^{-r_j}$, nonzero because $G_j(\alpha_j)\ne0$ and $\abs{\alpha_j}=1$. Hence $\deg Q_j=r_j-1$ and $P_j(n)=\alpha_j^{-n}(A_jn^{r_j-1}+O(n^{r_j-2}))$.
:::

:::

::: {.pf-step #conclusion}
$F_n=\sum_{j=1}^{k}P_j(n)+O(e^{-\epsilon n})$ with $\epsilon=\log\rho>0$.

::: pf-proof
Substituting the form of $P_j$ into (2) gives the expansion, and $\rho^{-n}=e^{-n\log\rho}=e^{-\epsilon n}$ with $\epsilon=\log\rho>0$ depending only on $F$. This is the corrected statement the card proves; each $P_j$ is $\alpha_j^{-n}$ times a polynomial of degree exactly $r_j-1$.
:::

:::

::: {.pf-step #corrections}
The printed statement needs the two corrections, and both are strict: the minus sign, and the factor $\alpha_j^{-n}$.

::: pf-proof
Sign: for $F(w)=1/(w-1)$ one has $F_n=-1$ for all $n$, while $\operatorname{res}_{w=1}(F(w)w^{-n-1})=1$; with the residue itself in place of $P_1$ the expansion fails for every $n$, so the minus sign belongs to the statement. Factor: for $F(w)=1/(w-i)$ there is one simple pole at $\alpha_1=i$ and $F_n=i(-i)^n$, which cycles through $i,1,-i,-1$; if $F_n=P(n)+O(e^{-\epsilon n})$ with a genuine polynomial $P$, then $P$ is constant here and $i(-i)^n\to c$, which a non-constant periodic sequence cannot do. Only when every $\alpha_j=1$ does $\alpha_j^{-n}=1$ and the printed wording hold literally.
:::

:::

::: {.pf-step #checks}
The formula reproduces the coefficients in three cases: $F=1/(w-1)^2$ gives $F_n=n+1=P_1(n)$; $F=1/((w-1)^2(w+1))$ gives $F_n=\frac n2+\frac34+\frac{(-1)^n}{4}=P_1(n)+P_2(n)$ with $\deg Q_1=1$ and $\deg Q_2=0$; and $F=1/(w-i)$ gives $F_n=P_1(n)$ exactly.

::: pf-proof
For $F=1/(w-1)^2$ the coefficient of $w^n$ is $n+1$, while the residue formula gives $P_1(n)=-\frac{d}{dw}[w^{-n-1}]_{w=1}=n+1$. For the second function partial fractions give the coefficient $\frac n2+\frac34+\frac{(-1)^n}{4}$, and the residues at $1$ and $-1$ give $\frac n2+\frac34$ and $\frac{(-1)^n}{4}$. For the third, $F$ is meromorphic on $\CC$, so $\rho$ and hence $\epsilon$ may be taken arbitrarily large for each fixed $n$; letting $\epsilon\to\infty$ gives $F_n=P_1(n)$ with no error term.
:::

:::

:::

:::
