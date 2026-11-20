---
schema: qual/card@1
id: E-SS8.PR-8
kind: problem
title: Bieberbach bound for real Taylor coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Univalent Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 8, §3, problem 8, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, parts (a)--(f); nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    All six parts. (a) Fourier coefficient of the odd function $v$; (b) induction;
    (c) $f(\bar z)=\overline{f(z)}$ and the sign of the imaginary part near $0$; (d) from the power
    series; (e) the estimate $\abs{a_n}r^n\le nr$ from (a) with $a_1=1$, which gives
    $\abs{a_n}\le n/r^{n-1}\to n$; (f) the Koebe function is univalent because
    $z/(1-z)^2=\frac14\bigl(\frac{1+z}{1-z}\bigr)^2-\frac14$ and squaring is injective on the right
    half-plane. Nothing is left in outline.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read against the printed item, Chapter 8, Problem 8 on printed p. 259 (PDF p. 278): the asterisk
    the print sets before "8." is recorded in the remark, and two clauses of the print that the
    statement had dropped are restored -- the attribution "Bieberbach conjectured that in fact
    $\abs{a_n}\le n$ for all $n\ge2$; this was proved by deBranges", and the conclusion
    $\abs{a_n}\le n$ of part (e). The rest of the statement is the print's, parts (a)--(f). Not
    checked: the argument, which this pass did not re-derive.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Repair of step s4 on the reader's report. The step bounded $\sum_{k\ge2}\abs{a_k}r^k$ by
    $r^2\sum_{k\ge2}\abs{a_k}$ and called the sum finite because $f$ is holomorphic on a
    neighbourhood of $\overline\DD$; that is not a hypothesis of the problem, and it is false for the
    card's own example $f(z)=z/(1-z)^2$, whose coefficients are $a_k=k$ and whose coefficient sum
    diverges. The bound now fixes $r_0<1$, uses the absolute convergence of $\sum_k\abs{a_k}r_0^k$
    inside the radius of convergence, and gets $\sum_{k\ge2}\abs{a_k}r^k\le Cr^2$ with
    $C=\sum_{k\ge2}\abs{a_k}r_0^{k-2}$ for $0<r\le r_0$, which is all that
    $v=r\sin\theta(1+O(r))$ needs. No other step changed. Provenance: no published solution set
    covers this Problem (Rhoades, *Solutions/Hints to the Exercises*, 2006, covers a selection of the
    Exercises), so the argument is the card's own.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Second repair of step s4, on the reader's report that the step's conclusion still did not
    follow. The previous bound $\abs{v-r\sin\theta}\le Cr^2$ does not give
    $v=r\sin\theta(1+O(r))$ uniformly in $\theta$: recovering the factor $1+O(r)$ means dividing by
    $\sin\theta$, and no bound uniform in $\theta$ survives that near $\theta=0$ and $\theta=\pi$.
    The step now estimates term by term with part (b), $\abs{\sin(k\theta)}\le k\sin\theta$, which
    gives $\abs{v-r\sin\theta}\le Cr^2\sin\theta$ with $C=\sum_{k\ge2}k\abs{a_k}r_0^{k-2}$ finite for
    any fixed $0<r_0<1$ because $\sum_k ka_kz^{k-1}$ is the termwise derivative of a series with
    radius of convergence at least $1$. The bound carries the factor $\sin\theta$ itself, so it is
    valid at the endpoints, and $v\sin\theta\ge r\sin^2\theta(1-Cr)$ settles the sign for small $r$;
    for the remaining $r$ the step invokes step s3, which gives $v>0$ on $(0,\pi)$ for every
    $0<r<1$. No other step changed, and the provenance sentence above stands: the argument is the
    card's own.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Published solution read and found not to repair the defect this card repairs. Wang Zirui,
    *Complete Solutions for Chapter 8* (SJTU), in the public repository
    `wzr-0831/stein-shakarchi-princeton-lectures-in-analysis-solutions`, Problem 8, covers parts
    (a)--(c) and (f) in outline and then, for part (d), states only that
    $v(r,\theta)=r\sin\theta[1+O(r)]$ for small $r$, "it is the upper side, so $v\sin\theta\ge0$ for
    all $r$" -- the same uniform inference from a bound without the factor $\sin\theta$ that the
    reader's report rejected. The published text is therefore recorded as carrying the defect, not as
    closing it, and step s4, which estimates $\abs{v-r\sin\theta}\le Cr^2\sin\theta$ term by term
    through $\abs{\sin(k\theta)}\le k\sin\theta$, remains the card's own. Checked: the quotation, read
    at the document's Problem 8. Not checked: anything in that document outside its Problem 8.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Step s3 rewritten, and the card now states that no published solution carries part (d). Step s3's
    proof said the set where $\operatorname{Im}f\ne0$ is $\DD^+\setminus f^{-1}(\RR)$ and that
    connectedness of $\DD^+$ gives the sign; the complement of a closed subset of a connected set need
    not be connected, so that was an assertion, not a proof. The step now argues on the image: an
    $f(z)\in\RR$ with $\operatorname{Im}z>0$ would give $f(\overline z)=\overline{f(z)}=f(z)$ at the
    distinct points $z,\overline z$ of the disc, against injectivity, so $f(\DD^+)$ misses the real
    axis; it is connected as a continuous image of the connected $\DD^+$; a connected subset of
    $\CC\setminus\RR$, which is a union of two disjoint open half-planes, lies in one of them; and
    $f(ir)=ir+r^2h(ir)$ has positive imaginary part for small $r$, which names the component as the
    upper half-plane. No nonvanishing derivative is used, only injectivity, continuity and the reality
    of the coefficients. Checked against Chapter 8, Problem 8(c) read in the book: the print asks for
    symmetry of $f(\DD)$ and for $f$ to carry the upper half-disc into one of the two parts of $f(\DD)$,
    and the step proves both, plus positivity of $v$ on the open rectangle. Not re-read in this pass:
    steps s1, s2 and s5--s6, and the argument of step s4 beyond its use of s3.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Parts (c) and (d) of the statement restored to the printed wording, which the card had compressed.
    Read in the book: the print's (c) is "Use the fact that $a_n\in\RR$ to show that $f(\DD)$ is
    symmetric with respect to the real axis, and use this fact to show that $f$ maps the upper
    half-disc into either the upper or lower part of $f(\DD)$", and its (d) is "Show that for $r$
    small, $v(r,\theta)=r\sin\theta[1+O(r)]$, and use the previous part to conclude that
    $v(r,\theta)\sin\theta\ge0$ for all $0<r<1$ and $0\le\theta\le\pi$". The card had written
    "Deduce that" in (d) and "and that" in (c), which drops the instruction to use part (c) -- the
    very step the repair of step s3 supplies -- so the wording now follows the print. No mathematics
    changed; the solution already uses part (c) for the sign.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Part (f) restored to the printed wording: the print asks to check that $f(z)=z/(1-z)^2$
    "satisfies all the hypotheses and that $\abs{a_n}=n$ for all $n$", and the card had written
    $a_n=n$. Step s6 proves the stronger $a_n=n$, which implies the printed claim. Two corrections to
    earlier events of this card, which stand as written: the event of 2026-11-01 places the item in
    "Chapter 8, §3", whereas the Problems of Chapter 8 are §6; and the event above says the Wang
    Zirui set covers "parts (a)--(c) and (f)" in outline, whereas it covers all six parts -- (a), (b),
    (c), (d) with the defective inference, (e) and (f) -- as read in
    `stein-shakarchi-book2-chapter08-solutions.tex` at its Problem 8. No mathematics changed.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Parts (c), (d) and (f) restored to the printed wording, word for word, read against Chapter 8,
    Problem 8 in the retained book. The print's (c) opens "Use the fact that $a_n\in\RR$ to show
    that $f(\DD)$ is symmetric with respect to the real axis", where the card had "Use $a_n\in\RR$"
    and "symmetric about"; the print's (d) puts the display after "Show that for $r$ small," where
    the card had "for small $r$" at the end of the sentence; and the print's (f) reads "Check that
    the function $f(z)=z/(1-z)^2$ satisfies all the hypotheses and that $\abs{a_n}=n$ for all $n$",
    where the card had "meets the hypotheses and has $\abs{a_n}=n$ for every $n$". The mathematical
    content of the three parts is unchanged, parts (a), (b) and (e) are untouched, and the asterisk
    remark is untouched.

---

::: {.exercise}
Let $f$ be injective and holomorphic on the unit disc, with $f(0)=0$ and $f'(0)=1$. Write $f(z)=z+a_2z^2+a_3z^3+\cdots$. Problem 1 in Chapter 3 shows that $\abs{a_2}\leq2$. Bieberbach conjectured that in fact $\abs{a_n}\leq n$ for all $n\geq2$; this was proved by deBranges. This problem outlines an argument to prove the conjecture under the additional assumption that the coefficients $a_n$ are real.

(a) For $z=re^{i\theta}$ with $0<r<1$, let $v(r,\theta)=\Im f(re^{i\theta})$. Show that
$$
a_nr^n=\frac2\pi\int_0^\pi v(r,\theta)\sin(n\theta)\,d\theta.
$$

(b) Show that $\abs{\sin(n\theta)}\leq n\sin\theta$ for $0\leq\theta\leq\pi$ and $n\geq1$.

(c) Use the fact that $a_n\in\RR$ to show that $f(\DD)$ is symmetric with respect to the real axis, and use this fact to show that $f$ maps the upper half-disc into either the upper or lower part of $f(\DD)$.

(d) Show that for $r$ small,
$$
v(r,\theta)=r\sin\theta[1+O(r)],
$$
and use the previous part to conclude that $v(r,\theta)\sin\theta\geq0$ for all $0<r<1$ and $0\leq\theta\leq\pi$.

(e) Prove that $\abs{a_nr^n}\leq nr$, and let $r\to1$ to conclude that $\abs{a_n}\leq n$.

(f) Check that the function $f(z)=z/(1-z)^2$ satisfies all the hypotheses and that $\abs{a_n}=n$ for all $n$.
:::

::: {.remark}
The book marks this problem with an asterisk (Chapter 8, Problem 8).
:::

::: {.solution}
No published solution carries part (d). The only located published solution of this Problem — Wang Zirui, *Complete Solutions for Chapter 8* (Problem 8), in the repository `wzr-0831/stein-shakarchi-princeton-lectures-in-analysis-solutions` — says of part (d) only that $v(r,\theta)=r\sin\theta[1+O(r)]$ for small $r$, "so" $v\sin\theta\ge0$ for all $r$: the very inference a reader rejected on this card, because a bound without the factor $\sin\theta$ cannot be divided by it near $\theta=0$ and $\theta=\pi$. The argument below is therefore the card's own, following the printed hints, and steps s2--s4 are where it does the work the printed hint leaves implicit.

Let $f(z)=z+a_2z^2+a_3z^3+\cdots$ be injective and holomorphic on $\DD$ with $f(0)=0$, $f'(0)=1$, and suppose every $a_n\in\RR$. For $0<r<1$ and $z=re^{i\theta}$ put $v(r,\theta)=\operatorname{Im}f(re^{i\theta})$.

::: pf

::: {.pf-step #s1}

Part (a): $a_nr^n=\dfrac2\pi\displaystyle\int_0^\pi v(r,\theta)\sin(n\theta)\,d\theta$ for $n\ge1$.

::: pf-proof

Since the $a_k$ are real, $f(re^{i\theta})=\sum_k a_kr^k(\cos k\theta+i\sin k\theta)$ with $a_1=1$, so $v(r,\theta)=\sum_{k\ge1}a_kr^k\sin k\theta$, uniformly convergent in $\theta$. Hence
$$
\frac2\pi\int_0^\pi v(r,\theta)\sin(n\theta)\,d\theta=\sum_{k\ge1}a_kr^k\cdot\frac2\pi\int_0^\pi\sin(k\theta)\sin(n\theta)\,d\theta=a_nr^n,
$$
because $\frac2\pi\int_0^\pi\sin(k\theta)\sin(n\theta)d\theta=\delta_{kn}$.

:::

:::

::: {.pf-step #s2}

Part (b): $\abs{\sin(n\theta)}\le n\sin\theta$ for $0\le\theta\le\pi$ and $n\ge1$.

::: pf-proof

For $n=1$ it is an equality. If it holds for $n-1$, then
$$
\abs{\sin(n\theta)}=\abs{\sin((n-1)\theta)\cos\theta+\cos((n-1)\theta)\sin\theta}\le(n-1)\sin\theta\abs{\cos\theta}+\abs{\cos((n-1)\theta)}\sin\theta\le n\sin\theta
$$
on $[0,\pi]$, where $\sin\theta\ge0$.

:::

:::

::: {.pf-step #s3}

Part (c): $f(\DD)$ is symmetric about the real axis; $f$ carries the upper half-disc $\DD^+$ into one of the two components of $\CC\setminus\RR$, namely the upper half-plane; hence $v(r,\theta)>0$ for $0<r<1$ and $0<\theta<\pi$.

::: pf-proof

Since every $a_k$ is real, $f(\overline z)=\overline{f(z)}$ for $\abs z<1$, because the series converges at $\overline z$ and conjugation is continuous. Hence $f(\DD)$ is invariant under $z\mapsto\overline z$, that is, symmetric about $\RR$.

Two facts about $f(\DD^+)$, where $\DD^+=\{z:\abs z<1,\ \operatorname{Im}z>0\}$. First, $f(\DD^+)\cap\RR=\varnothing$: if $z\in\DD^+$ and $f(z)\in\RR$, then $\overline z\in\DD$ with $\overline z\ne z$ and $\operatorname{Im}\overline z<0$, while $f(\overline z)=\overline{f(z)}=f(z)$, contradicting injectivity. Second, $f(\DD^+)$ is connected, being the image of the connected set $\DD^+$ under the continuous map $f$.

The set $\CC\setminus\RR$ has exactly two components, the open upper and lower half-planes. A connected subset of the union of two disjoint open sets lies in one of them, so $f(\DD^+)$ is contained in one component.

Which component it is, the point $i r$ decides. Since $f(0)=0$ and $f'(0)=1$, one has $f(z)=z+z^2h(z)$ with $h$ holomorphic on $\DD$; then
$$
\operatorname{Im}f(ir)=r-r^2\operatorname{Im}h(ir),
$$
so $\operatorname{Im}f(ir)>0$ for all $0<r$ with $r\operatorname{Im}h(ir)<1$, which holds for small $r$ because $h$ is bounded on a neighbourhood of $0$. That point of $f(\DD^+)$ lies in the upper half-plane, so the component is the upper half-plane.

Therefore $\operatorname{Im}f(z)>0$ on $\DD^+$, that is, $v(r,\theta)>0$ for $0<r<1$ and $0<\theta<\pi$. Also $v(r,0)=v(r,\pi)=0$, because $f$ maps $\DD\cap\RR$ into $\RR$ by the reality of the coefficients.

:::

:::

::: {.pf-step #s4}

Part (d): there are constants $C<\infty$ and $r_0>0$ such that
$$
\abs{v(r,\theta)-r\sin\theta}\le Cr^2\sin\theta
$$
for $0<r\le r_0$ and every $\theta\in[0,\pi]$. Hence $v(r,\theta)=r\sin\theta\,(1+O(r))$ as $r\to0$, with the $O(r)$ uniform in $\theta$, and consequently $v(r,\theta)\sin\theta\ge0$ for $0<r<1$ and $0\le\theta\le\pi$.

::: pf-proof

Since every $a_k$ is real and $a_1=1$,
$$
v(r,\theta)=\sum_{k\ge1}a_kr^k\sin(k\theta),\qquad v(r,\theta)-r\sin\theta=\sum_{k\ge2}a_kr^k\sin(k\theta).
$$
Fix $0<r_0<1$. The series $\sum_k a_kz^k$ has radius of convergence at least $1$, because $f$ is holomorphic on $\DD$, so its termwise derivative $\sum_k ka_kz^{k-1}$ converges absolutely at $z=r_0$, that is,
$$
C\coloneqq\sum_{k\ge2}k\abs{a_k}r_0^{k-2}<\infty .
$$
In particular $\sum_{k\ge2}\abs{a_k}r^k\abs{\sin(k\theta)}$ converges for $0<r\le r_0$, so the difference may be estimated term by term; and step [](#s2){.pf-ref} gives $\abs{\sin(k\theta)}\le k\sin\theta$ for $0\le\theta\le\pi$. Therefore
$$
\abs{v(r,\theta)-r\sin\theta}\le\sum_{k\ge2}\abs{a_k}r^k\abs{\sin(k\theta)}\le\sin\theta\sum_{k\ge2}k\abs{a_k}r^k\le Cr^2\sin\theta
$$
for $0<r\le r_0$ and $0\le\theta\le\pi$, the last step because $k\abs{a_k}r^k=r^2\bigl(k\abs{a_k}r^{k-2}\bigr)\le r^2k\abs{a_k}r_0^{k-2}$.

Writing $R(r,\theta)=v(r,\theta)-r\sin\theta$, dividing the display by $r\sin\theta$ for $0<\theta<\pi$ gives $v=r\sin\theta\,(1+\varepsilon)$ with $\abs{\varepsilon}\le Cr$; at $\theta=0$ and $\theta=\pi$ both $v(r,\theta)$ and $r\sin\theta$ vanish, so the display still holds there. Multiplying by $\sin\theta\ge0$,
$$
v(r,\theta)\sin\theta=r\sin^2\theta+R(r,\theta)\sin\theta\ge r\sin^2\theta-Cr^2\sin^2\theta=r\sin^2\theta\,(1-Cr),
$$
which is non-negative for $0<r\le r_0$ with $Cr\le1$ (and for every $0<r\le r_0$ when $C=0$). For the remaining $r$, step [](#s3){.pf-ref} gives $v(r,\theta)>0$ whenever $0<\theta<\pi$ and $0<r<1$, while $v(r,\theta)\sin\theta=0$ at $\theta=0$ and $\theta=\pi$ because $\sin\theta=0$. Hence $v(r,\theta)\sin\theta\ge0$ for all $0<r<1$ and $0\le\theta\le\pi$.

:::

:::

::: {.pf-step #s5}

Part (e): $\abs{a_n}r^n\le nr$ for $0<r<1$, hence $\abs{a_n}\le n$.

::: pf-proof

By step [](#s1){.pf-ref}, steps [](#s2){.pf-ref} and [](#s4){.pf-ref},
$$
\abs{a_n}r^n=\abs{\frac2\pi\int_0^\pi v\sin(n\theta)\,d\theta}\le\frac2\pi\int_0^\pi\abs{v}\abs{\sin(n\theta)}\,d\theta\le\frac{2n}{\pi}\int_0^\pi v\sin\theta\,d\theta .
$$
By step [](#s1){.pf-ref} with $n=1$ and $a_1=1$, the last integral equals $\frac\pi2\cdot r$. Hence $\abs{a_n}r^n\le nr$, that is $\abs{a_n}\le n/r^{n-1}$ for every $0<r<1$. Letting $r\to1$ gives $\abs{a_n}\le n$.

:::

:::

::: {.pf-step #s6}

Part (f): $f(z)=\dfrac{z}{(1-z)^2}$ satisfies the hypotheses, with $a_n=n$ for every $n$.

::: pf-proof

The expansion $\frac{z}{(1-z)^2}=\sum_{n\ge1}nz^n$ holds for $\abs z<1$, so $f(0)=0$, $f'(0)=1$ and $a_n=n\in\RR$.

For injectivity, write
$$
f(z)=\frac{z}{(1-z)^2}=\frac14\Bigl(\frac{1+z}{1-z}\Bigr)^2-\frac14 .
$$
The map $z\mapsto\frac{1+z}{1-z}$ is a biholomorphism of $\DD$ onto the right half-plane $\{\Re w>0\}$, and squaring is injective there: if $w_1^2=w_2^2$ with $\Re w_j>0$, then $w_1=\pm w_2$, and the sign must be positive because both have positive real part. Hence $f$ is injective on $\DD$.

:::

:::

:::

:::
