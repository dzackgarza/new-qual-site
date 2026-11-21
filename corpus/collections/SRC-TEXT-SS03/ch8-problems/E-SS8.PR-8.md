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
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Solution replaced by a transcription, on the reader's report that the card called its argument
    its own. The proof now follows Wang Zirui, *Complete Solutions for Chapter 8*, Problem 8 (file
    `stein-shakarchi-book2-chapter08-solutions.tex`, commit `876542f9cea2`), sentence by sentence:
    sine orthogonality for (a), induction from the addition formula for (b), reflection symmetry plus
    injectivity for (c), the series of $v$ at small $r$ for (d), the integral bound for (e), the Koebe
    function for (f), and each step names the published sentence it transcribes and says where it
    supplies the detail that sentence compresses. The published part-(d) sentence infers
    $v\sin\theta\ge0$ from $v=r\sin\theta[1+O(r)]$ with no factor $\sin\theta$, so that step is kept
    as published, and the correction -- the bound $\abs{v-r\sin\theta}\le Cr^2\sin\theta$ that
    Chapter 8, Problem 8(b) yields -- is stated in a remark after the solution that cites the printed
    part (d). The sentences of the earlier events saying that the argument is the card's own record
    the state at their dates and no longer describe the solution.

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
This solution is a transcription of Wang Zirui, *Complete Solutions for Chapter 8*, Problem 8, in the repository `wzr-0831/stein-shakarchi-princeton-lectures-in-analysis-solutions` (file `stein-shakarchi-book2-chapter08-solutions.tex`, read at commit `876542f9cea2`). The published outline disposes of the six parts in a few sentences: part (a) by sine orthogonality, part (b) by induction from the addition formula, part (c) by reflection symmetry together with injectivity, part (d) from the series of $v$ at small $r$, part (e) from (a), (b) and the sign of $v\sin\theta$, and part (f) by exhibiting the Koebe function. Each step below is one of those sentences, and says where the sentence compresses an estimate that its claim needs. The set is not retained in this checkout and was read at its source. Part (d) is the one place where the published sentence does not establish what the book asks, and the remark after this solution records the correction.

Let $f(z)=z+a_2z^2+a_3z^3+\cdots$ be injective and holomorphic on $\DD$ with $f(0)=0$, $f'(0)=1$, and suppose every $a_n\in\RR$. For $0<r<1$ and $z=re^{i\theta}$ put $v(r,\theta)=\operatorname{Im}f(re^{i\theta})$.

::: pf

::: {.pf-step #s1}

Part (a): $v(r,\theta)=\sum_{k\ge1}a_kr^k\sin(k\theta)$, and sine orthogonality gives
$$
a_nr^n=\frac2\pi\int_0^\pi v(r,\theta)\sin(n\theta)\,d\theta .
$$

::: pf-proof

Since every $a_k$ is real, $f(re^{i\theta})=\sum_k a_kr^k(\cos k\theta+i\sin k\theta)$ with $a_1=1$, so $v(r,\theta)=\sum_{k\ge1}a_kr^k\sin(k\theta)$, and the series converges uniformly in $\theta$ for fixed $r<1$ because $\sum_k\abs{a_k}r^k$ converges. Termwise integration is therefore legitimate, and $\frac2\pi\int_0^\pi\sin(k\theta)\sin(n\theta)\,d\theta=\delta_{kn}$ gives the display.

:::

:::

::: {.pf-step #s2}

Part (b): $\abs{\sin(n\theta)}\le n\sin\theta$ for $0\le\theta\le\pi$ and $n\ge1$.

::: pf-proof

The published sentence is "induction from the addition formula". For $n=1$ the inequality is an equality. If it holds for $n-1$, then
$$
\abs{\sin(n\theta)}=\abs{\sin((n-1)\theta)\cos\theta+\cos((n-1)\theta)\sin\theta}\le(n-1)\sin\theta\abs{\cos\theta}+\abs{\cos((n-1)\theta)}\sin\theta\le n\sin\theta
$$
on $[0,\pi]$, where $\sin\theta\ge0$.

:::

:::

::: {.pf-step #s3}

Part (c): real coefficients give $f(\overline z)=\overline{f(z)}$, so $f(\DD)$ is symmetric with respect to the real axis; and injectivity makes the upper half-disc map wholly into one of the two components of $\CC\setminus\RR$.

::: pf-proof

Because every $a_k$ is real, $f(\overline z)=\sum_k a_k\overline z^k=\overline{\sum_k a_kz^k}=\overline{f(z)}$ for $\abs z<1$, conjugation being continuous; hence $f(\DD)$ is invariant under $z\mapsto\overline z$, that is, symmetric with respect to $\RR$.

For the second assertion let $\DD^+=\{z:\abs z<1,\ \operatorname{Im}z>0\}$. First, $f(\DD^+)\cap\RR=\varnothing$: if $z\in\DD^+$ and $f(z)\in\RR$, then $\overline z\in\DD$ with $\overline z\ne z$ and $\operatorname{Im}\overline z<0$, while $f(\overline z)=\overline{f(z)}=f(z)$, contradicting injectivity. Second, $f(\DD^+)$ is connected, being the image of the connected set $\DD^+$ under the continuous map $f$. A connected subset of $\CC\setminus\RR$, the union of the two disjoint open half-planes, lies in one of them.

:::

:::

::: {.pf-step #s4}

Part (d): $v(r,\theta)=r\sin\theta[1+O(r)]$ for small $r$, and it is the upper side, so $v(r,\theta)\sin\theta\ge0$ for all $0<r<1$ and $0\le\theta\le\pi$.

::: pf-proof

The published sentence is "since $v(r,\theta)=r\sin\theta[1+O(r)]$ for small $r$, it is the upper side, so $v\sin\theta\ge0$ for all $r$". Its two ingredients are these. Since $a_1=1$ and every $a_k$ is real,
$$
v(r,\theta)-r\sin\theta=\sum_{k\ge2}a_kr^k\sin(k\theta),
$$
and for fixed $0<r\le r_0<1$ the right-hand side is bounded by $r^2\sum_{k\ge2}\abs{a_k}r_0^{k-2}$, a finite sum because $\sum_k\abs{a_k}r_0^k$ converges; hence $v(r,\theta)=r\sin\theta[1+O(r)]$ as $r\to0$ for each fixed $\theta$. Next, $f(ir)=ir+O(r^2)$ has positive imaginary part for small $r>0$, so the component of step [](#s3){.pf-ref} that contains $f(\DD^+)$ is the upper half-plane, which is what "it is the upper side" names; in particular $v(r,\theta)>0$ for $0<\theta<\pi$.

The published text then reads the sign off the display. Read at fixed $\theta$ that reading is complete, and the step's last two sentences supply what it compresses: for $0<\theta<\pi$ the quotient $v(r,\theta)/(r\sin\theta)$ tends to $1$, so $v>0$ for small $r$; the component is therefore the upper one; and step [](#s3){.pf-ref} then gives $v>0$ at every $0<r<1$. At $\theta=0$ and $\theta=\pi$ one has $v(r,\theta)=0$, because $f$ maps $\DD\cap\RR$ into $\RR$ by the reality of the coefficients. Hence $v(r,\theta)\sin\theta\ge0$ on the whole rectangle. What the display does not carry is an estimate uniform in $\theta$, and the remark after this solution states the $\sin\theta$-weighted form of it that the printed part (b) yields.

:::

:::

::: {.pf-step #s5}

Part (e): $\abs{a_n}r^n\le nr$ for $0<r<1$, hence $\abs{a_n}\le n$.

::: pf-proof

The published sentence is "consequently $\abs{a_n}r^n\le\frac{2n}\pi\int_0^\pi v(r,\theta)\sin\theta\,d\theta=nr$". By step [](#s1){.pf-ref}, steps [](#s2){.pf-ref} and [](#s4){.pf-ref},
$$
\abs{a_n}r^n=\abs{\frac2\pi\int_0^\pi v\sin(n\theta)\,d\theta}\le\frac2\pi\int_0^\pi\abs{v}\abs{\sin(n\theta)}\,d\theta\le\frac{2n}\pi\int_0^\pi v\sin\theta\,d\theta,
$$
the last step because $v\sin\theta\ge0$ and $\abs{\sin(n\theta)}\le n\sin\theta$ with $\sin\theta\ge0$. By step [](#s1){.pf-ref} with $n=1$ and $a_1=1$, the last integral equals $\frac\pi2r$, so $\abs{a_n}r^n\le nr$ and $\abs{a_n}\le n/r^{n-1}$ for every $0<r<1$; letting $r\uparrow1$ gives $\abs{a_n}\le n$.

:::

:::

::: {.pf-step #s6}

Part (f): the Koebe function $f(z)=\dfrac{z}{(1-z)^2}$ is injective, has real coefficients, and $\abs{a_n}=n$ for every $n$.

::: pf-proof

The published sentence is that $z/(1-z)^2=\sum_{n\ge1}nz^n$ "is injective, has real coefficients, and attains equality for every $n$". The expansion $\frac{z}{(1-z)^2}=\sum_{n\ge1}nz^n$ holds for $\abs z<1$, so $f(0)=0$, $f'(0)=1$ and $a_n=n\in\RR$ with $\abs{a_n}=n$. For injectivity, write
$$
f(z)=\frac{z}{(1-z)^2}=\frac14\Bigl(\frac{1+z}{1-z}\Bigr)^2-\frac14 .
$$
The map $z\mapsto\frac{1+z}{1-z}$ is a biholomorphism of $\DD$ onto the right half-plane $\{\Re w>0\}$, and squaring is injective there: if $w_1^2=w_2^2$ with $\Re w_j>0$, then $w_1=\pm w_2$, and the sign is positive because both have positive real part.

:::

:::

:::

:::

::: {.remark title="Correction to the published estimate in part (d)"}
The published sentence draws the sign of $v\sin\theta$ from the display $v(r,\theta)=r\sin\theta[1+O(r)]$, whose error carries no factor $\sin\theta$. Read at fixed $\theta$ the display is enough, and the argument of part (d) records how; what it does not give is an estimate uniform in $\theta$, for its implied constant may depend on $\theta$, and even a bound $\abs{v-r\sin\theta}\le Cr^2$ holding uniformly in $\theta$ cannot be divided by $\sin\theta$ near $\theta=0$ and $\theta=\pi$, where both sides vanish. The printed part (b) supplies the missing factor. With $C=\sum_{k\ge2}k\abs{a_k}r_0^{k-2}<\infty$ for a fixed $0<r_0<1$, which is finite because $\sum_kka_kz^{k-1}$ is the termwise derivative of a series whose radius of convergence is at least $1$,
$$
\abs{v(r,\theta)-r\sin\theta}\le\sum_{k\ge2}\abs{a_k}r^k\abs{\sin(k\theta)}\le\sin\theta\sum_{k\ge2}k\abs{a_k}r^k\le Cr^2\sin\theta
$$
for $0<r\le r_0$ and $0\le\theta\le\pi$, so that $v\sin\theta\ge r\sin^2\theta(1-Cr)\ge0$ once $Cr\le1$, the remaining $r$ being covered by part (c). That is the $\sin\theta$-weighted form of the estimate, and it proves Chapter 8, Problem 8(d) as printed from the display alone; the transcription above is left as the published text has it.
:::
