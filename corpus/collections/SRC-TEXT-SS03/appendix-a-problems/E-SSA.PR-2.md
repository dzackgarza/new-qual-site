---
schema: qual/card@1
id: E-SSA.PR-2
kind: problem
title: Stirling's formula with an asymptotic expansion in powers of $s^{-1}$
classification:
  areas:
  - complex-analysis
  topics:
  - Asymptotics
  - Gamma Function
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 2,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Solution installed: the expansion is obtained from the exact substitution Phi = v^2/2 near x = 1, with A(v) = v/(x(v)-1) giving the coefficients a_j = alpha_{2j}(2j-1)!! and a_1 = 1/12, a Gaussian cut-off Watson lemma for the remainder, and the tails estimated by the book's iteration for e^{-s Phi}. The stated range Re s >= 1/2 is extended to Re s >= 0 through Gamma(s+1) = s Gamma(s).
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Locator correction to the events above: Appendix A's Problems occupy PDF pp. 360--362 of the
    retained scan, printed pp. 341--343, not PDF pp. 359--363; PDF p. 359 is printed p. 340 and
    PDF p. 363 is the Appendix B title page. This item was not otherwise re-read in this pass, and it
    carries no asterisk -- the print's Appendix A mark is before Problem 5 only.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Repair of step `watson` on the reader's report. The step set $R=B\chi-P$ and called
    $R\in C_c^\infty(\RR)$ with support in $[-2\rho,2\rho]$; that is false, because $B\chi$ is
    compactly supported but the polynomial $P$ is not, so outside $\operatorname{supp}\chi$ the
    function $R$ equals $-P$ and does not have compact support. The step now sets $B_1=B\chi$, notes
    that $B_1\in C_c^\infty$ with the same support and the same Taylor coefficients at $0$ as $B$,
    and forms $R=B_1-P$, which is compactly supported, vanishes to order $2K+2$ at $0$, and is the
    function whose Gaussian integral is estimated; the integral is unchanged because $B\chi=B_1$.
    The integration-by-parts estimate and the finiteness of $\int\abs{D^{K+1}R}$ then follow as
    written. No other step changed. Provenance: no published solution set covers this Problem
    (Rhoades, *Solutions/Hints to the Exercises*, 2006, covers a selection of the Exercises), so the
    argument is the card's own.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    The repair of step `watson` recorded above did not hold, and is replaced on a referee's report of
    this session: renaming $B$ as $B\chi$ leaves $R=B\chi-P$ equal to $-P$ off
    $\operatorname{supp}\chi$, so $R$ is still not compactly supported. The step now splits
    $B\chi=P+R-Q$ with $R=\chi(B-P)$, which is compactly supported and vanishes to order $2K+2$ at
    $0$, and $Q=P(1-\chi)$, which vanishes identically near $0$ but is only of polynomial growth at
    infinity; the integration-by-parts identity is stated under the weaker hypothesis that
    $e^{-\sigma_0v^2/2}g/v\to0$ at infinity, so it applies to both, and the two remainders are
    bounded by $C_R\abs{s}^{-K-1}$ and $C_Q\abs{s}^{-K-1}$. The step's statement, the moments
    computation and every other step are unchanged.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Record of the search behind the solution's provenance sentence, which the reader asked for where
    no published solution set covers the Problem. Read: the head of R. C. Rhoades,
    *Solutions/Hints to the Exercises from Complex Analysis by Stein and Shakarchi* (2006), whose
    abstract describes it as solutions or hints to "many of the exercises", with one part per
    chapter. Searched the open web for a set answering the end-of-chapter Problems of this book: no
    document answering Appendix A, Problem 2 was found. This search located no published set
    answering this Problem, and none is retained in this repository. Not checked: whether such a set
    exists outside what a web search reaches. The mathematics of the card is unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Provenance corrected: a published solution of this Problem was located, so the sentence saying
    that none existed is replaced. The set is Wang Zirui, *Complete Solutions for Appendix A*, in the
    public repository `wzr-0831/stein-shakarchi-princeton-lectures-in-analysis-solutions`, read at its
    Problem 2 and checked against Appendix A, Problem 2: it applies Euler--Maclaurin to $\log\Gamma$
    in a fixed sector, uses its Problem 1 for the endpoint remainder, exponentiates the resulting
    finite expansion, and identifies $a_1=1/12$ from $B_2/(2s)$. That answers the Problem, which asks
    only for the expansion and for the constants. The card's proof reaches the same expansion by a
    different route, the Laplace method of Appendix A section 5 on the integral representation, with
    the local expansion, Watson's lemma and the reflection formula for the left half-plane; it is
    therefore not a transcription, and is labelled as the card's own here. Not checked: anything in
    the published document outside its Problem 2, and no claim that the two routes' constants agree
    beyond $a_1$, which both state.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Solution replaced by a transcription, on the reader's report that the card called its argument its
    own. The proof now takes the published route of Wang Zirui, *Complete Solutions for Appendix A*,
    Problem 2 (file `stein-shakarchi-book2-appendix-a-solutions.tex`, commit `876542f9cea2`): the
    Euler--Maclaurin formula applied to $\log\Gamma$, the constant fixed by the Gaussian evaluation in
    the leading-order Stirling formula, the finite series exponentiated, and $a_1=1/12$ read off the
    first Bernoulli term $B_2/(2s)=1/(12s)$. Each step carries the published sentence as its claim and
    supplies the estimate that sentence compresses. The constant is identified with Appendix A,
    Theorem 2.3 instead of by a second Gaussian evaluation, and the expansion is carried from the
    right half-plane, where the summation formula holds, to the rest of $S_\delta$ by the recurrence
    and reflection formulas for $\Gamma$, which the published sentence folds into the words "in the
    fixed sector". Two divergences from the published text are stated on the card: the remainder the
    derivation gives is $O(\abs{s}^{1-2M})$, one power weaker than the published $O(\abs{s}^{-2M-1})$
    and sufficient for the printed $O(s^{-N})$, and the published sentence attributes the control of
    the remainder to Problem 1 of Appendix A, which this route does not use. The Laplace-method steps
    and the citation of Appendix A, §5 are gone with the old proof; the reflection step now derives
    its identity from Theorem 1.4 and Lemma 1.2 of Chapter 6, where the book itself points for it.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Three gaps in the transcribed proof repaired on the readers' reports (issue #172 by v085, and the
    report of #164 by gloc), with the transcription of Wang Zirui, *Complete Solutions for Appendix
    A*, Problem 2, kept. (1) Step `identify` compared the two expansions only to order $t^{-N}$,
    which fixes $b_n=(-1)^na_n$ for $n\le N-1$ and not for $n=N$; steps `left` and `identify` now
    carry the comparison one order further, to $O(\abs{s}^{-N-1})$ -- which the reflection estimate
    already supplies, its error being exponentially small -- and the coefficients are recovered by an
    induction in $u=1/t$, since multiplying by $t^n$ multiplies the terms of index $j<n$ rather than
    isolating $c_n$. (2) Step `right` chose $M$ with $2M-1\ge N+1$ alone, which admits $M<N$ (for
    $N=10$, $M=6$) while the proof truncates the exponent at $c_N$; $M$ is now also required to
    satisfy $M\ge N$, and the difference of $z$ from $\sum_{k\le N}c_ks^{1-2k}$ is then of order
    $\abs{s}^{-2N-1}$ as the step states. (3) The Euler limit is Chapter 6, Exercise 1, and step
    `log-expansion` now cites that Exercise instead of Chapter 6, §1. Each step of the proof now
    names at its head whether its claim is a sentence of the published solution or the card's own:
    the Euler--Maclaurin derivation, the estimates in `log-expansion` and `right`, the reduction of
    the constant to Appendix A, Theorem 2.3, and steps `reflection`, `left` and `identify` are the
    card's own, the last three by the same two identities the book uses for the same passage in its
    proof of Theorem 2.3. Checked in the retained book: Appendix A, Theorem 2.3 and its proof;
    Chapter 6, Exercise 1, Theorem 1.4 and Lemma 1.2. No problem statement changed and no citation
    changed except the one in item (3).
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Two items of the #172 reader's report at `437a029321` repaired; the choice $M=\max(N,2)$, the
    citation of Chapter 6, Exercise 1, the provenance markings and every other citation are
    unchanged. (1) Step `left` no longer infers a lower bound for the polynomial $\Psi_N$ from
    continuity: the report is right that "$F$ having no zeros" bounds $F(-s)$ only, and
    $\Psi_N(-1/s)$ may vanish on the compact remainder, so the reciprocal estimate did not follow.
    The step now sets $A_N=\sum_j\abs{a_j}$ in the preamble, chooses $R_N\ge4+2A_N$ so large that
    the remainder of step `right` at $-s$ is at most $1/4$, and proves $\abs{\Psi_N(-1/s)-1}\le
    A_N/\abs{s}\le\frac12$ and $\abs{F(-s)}\ge\frac14$ uniformly on the whole set
    $\{\Re(s)\le0,\ \abs{s}\ge R_N\}$; the split into an infinity argument and a compact remainder,
    and with it the appeal to continuity, is gone, and steps `identify` and the final qed now use
    $R_N$ in place of $4$. The published sentence "Apply the Euler--Maclaurin formula to
    $\log\Gamma(s)$ in the fixed sector $S_\delta$" is quoted at the step's head and the step says
    that it asserts the sectorial expansion without a word about the reciprocal of $\Psi_N$, so the
    bound is the card's own. (2) The logarithmic identity is no longer carried from $(0,\infty)$ to
    $\Re(s)>0$ "by continuity": the step defines $L_n(s)=\log n!+s\Log n-\sum_k\Log(s+k)$, shows
    $L_{n+1}-L_n=s/(n(n+1))+O(\abs{s}^2/n^2)$ so that $L=\lim L_n$ is holomorphic, obtains
    $e^L=\Gamma$ from Chapter 6, Exercise 1 -- hence $\Gamma$ has no zeros on the half-plane and a
    branch of $\log\Gamma$ exists there -- and concludes from agreement on the open set
    $(0,\infty)$ by the identity theorem, Corollary 4.9 of Chapter 2. Read in the retained book for
    this pass: Chapter 2, Theorem 4.8 and Corollary 4.9; Chapter 6, Exercise 1, which states the
    Euler limit for $s\ne0,-1,-2,\ldots$; and Wang's Appendix A, Problem 2 solution. The $A_N$ and
    $R_N$ bound, the normal-convergence estimate and the continuation are the card's own.
---

::: {.exercise}
The following is a more precise version of Stirling's formula. There are real constants $a_1=1/12$, $a_2,\dots,a_n,\dots$, so that for every $N>0$
$$
\Gamma(s)=e^{s\log s}e^{-s}\frac{\sqrt{2\pi}}{s^{1/2}}\Bigl(1+\sum_{j=1}^{N}a_js^{-j}+O(s^{-N})\Bigr)\qquad\text{when } s\in S_\delta .
$$
This can be proved by using the results of Problem 1 in place of Proposition 1.3.
:::

::: {.remark}
Appendix A sets its asterisk before Problem 5 only, so none stands before this problem (Appendix A, Problem 2).
:::

::: {.solution}
This solution is a transcription of Wang Zirui, *Complete Solutions for Appendix A*, Problem 2, in the repository `wzr-0831/stein-shakarchi-princeton-lectures-in-analysis-solutions` (file `stein-shakarchi-book2-appendix-a-solutions.tex`, read at commit `876542f9cea2`). The published solution gives the route in five sentences: apply the Euler--Maclaurin formula to $\log\Gamma(s)$ in the fixed sector $S_\delta$; read off, for every $M$,
$$
\log\Gamma(s)=\Bigl(s-\frac12\Bigr)\Log s-s+\frac12\log(2\pi)+\sum_{k=1}^{M}\frac{B_{2k}}{2k(2k-1)s^{2k-1}}+O\bigl(\abs{s}^{-2M-1}\bigr),
$$
fix the constant by the Gaussian evaluation in the leading-order Stirling formula; exponentiate the finite series, which gives real coefficients $a_j$ with
$$
\Gamma(s)=e^{s\Log s-s}\frac{\sqrt{2\pi}}{s^{1/2}}\Bigl(1+\sum_{j=1}^{N}a_js^{-j}+O(s^{-N-1})\Bigr),
$$
and read $a_1=1/12$ off the first term $B_2/(2s)=1/(12s)$ of the sum. The steps below are those sentences in order; each step says at its head whether its claim is a sentence of the published solution or the card's own, and which estimate it supplies that its sentence compresses. The passage from the right half-plane, where the summation formula is available, to the rest of $S_\delta$, which the published sentence folds into the words "in the fixed sector", is the work of steps [](#reflection){.pf-ref}, [](#left){.pf-ref} and [](#identify){.pf-ref}. The set is not retained in this checkout and was read at its source.

Two differences between the published text and the proof below are recorded here rather than inside the steps. The published display states the remainder as $O(\abs{s}^{-2M-1})$, while the Euler--Maclaurin estimate of step [](#log-expansion){.pf-ref} gives $O(\abs{s}^{1-2M})$, one power weaker; that is enough for the Problem, whose $O(s^{-N})$ is reached by choosing $M$ after $N$. And the published solution writes the expansion on the whole sector at once, whereas the summation formula holds on $\Re s>0$; steps [](#reflection){.pf-ref} to [](#identify){.pf-ref} carry the expansion across the imaginary axis by the recurrence and reflection formulas for $\Gamma$.

The printed hint for this Problem says it can be proved by using the results of Problem 1 of Appendix A in place of Proposition 1.3. The transcribed route does not use Problem 1: it controls the remainder with the Bernoulli estimate of the summation formula itself, and it fixes the constant by Theorem 2.3 of Appendix A, the leading-order formula proved there by the Laplace method and the Gaussian evaluation $\int_\RR e^{-x^2}dx=\sqrt\pi$; that is the "Gaussian evaluation in the leading-order Stirling formula" the published sentence names.

We write $\Log$ for the principal branch of the logarithm and $s^{\alpha}$ for the power defined by it, take $\delta>0$, and set $S_\delta=\{s:\abs{\arg s}\le\pi-\delta\}$ as in Appendix A, §2. The Bernoulli numbers satisfy $B_0=1$, $B_1=-\frac12$, $B_2=\frac16$, $B_4=-\frac1{30}$ and $B_{2k+1}=0$ for $k\ge1$; $B_{2k}(t)$ is the Bernoulli polynomial and $P_{2k}(x)\coloneqq B_{2k}(\{x\})$ its periodization, so that $\abs{P_{2k}}\le\abs{B_{2k}}$ and $P_{2k}=P'_{2k+1}$ away from the integers. Set
$$
c_k\coloneqq\frac{B_{2k}}{2k(2k-1)}\quad(k\ge1),\qquad \Psi_N(u)\coloneqq\sum_{j=0}^{N}a_ju^{j},
$$
where $a_0=1$ and, for $N\ge1$, the numbers $a_1,\ldots,a_N$ are those of the Taylor polynomial at $0$ of $\exp\bigl(\sum_{k\ge1}c_ku^{2k-1}\bigr)$: that is,
$$
\exp\Bigl(\sum_{k=1}^{N}c_ku^{2k-1}\Bigr)=\sum_{j=0}^{N}a_ju^{j}+O\bigl(\abs{u}^{N+1}\bigr)\qquad(u\to0),
$$
so $a_j$ depends only on $c_1,\ldots,c_j$. For $N\ge1$ put $A_N\coloneqq\sum_{j=1}^{N}\abs{a_j}$, so that $\abs{\Psi_N(u)-1}\le A_N\abs{u}$ whenever $\abs{u}\le1$. Finally $F(s)\coloneqq\sqrt{s/(2\pi)}\,\Gamma(s)e^{-s\Log s+s}$, which is meromorphic on $\CC\setminus(-\infty,0]$, with poles at the non-positive integers and no zeros.

::: pf

::: {.pf-step #euler-maclaurin}

Let $0\le a<b$ be integers, $M\ge1$ and $f\in C^{2M}\bigl([a,b]\bigr)$. Then
$$
\sum_{k=a}^{b}f(k)=\int_a^bf(x)\,dx+\frac{f(a)+f(b)}{2}+\sum_{r=1}^{M}\frac{B_{2r}}{(2r)!}\Bigl(f^{(2r-1)}(b)-f^{(2r-1)}(a)\Bigr)+R_M,
$$
where
$$
R_M=-\int_a^b\frac{P_{2M}(x)}{(2M)!}f^{(2M)}(x)\,dx,\qquad\text{so}\qquad \abs{R_M}\le\frac{\abs{B_{2M}}}{(2M)!}\int_a^b\abs{f^{(2M)}(x)}\,dx .
$$

::: pf-proof

The published solution invokes the Euler--Maclaurin summation formula without proof; the derivation below is the card's own. The starting point is
$$
\sum_{k=a}^{b}f(k)-\int_a^bf(x)\,dx-\frac{f(a)+f(b)}{2}=\int_a^bP_1(x)f'(x)\,dx,
$$
an integration by parts on each interval $[k,k+1]$, where $P_1(x)=\{x\}-\frac12$ and $P_1'=1$ away from the integers. One further integration by parts, with $P_1=P'_2/2$ and $P_2(a)=P_2(b)=B_2$, turns the right-hand side into $\frac{B_2}{2!}\bigl(f'(b)-f'(a)\bigr)-\int_a^bP_2f''/2!$, which is the display for $M=1$. For $M\ge2$ the passage from $M-1$ to $M$ is
$$
-\int_a^b\frac{P_{2M-2}f^{(2M-2)}}{(2M-2)!}
=\int_a^b\frac{P_{2M-1}f^{(2M-1)}}{(2M-1)!}
=\frac{B_{2M}}{(2M)!}\Bigl(f^{(2M-1)}(b)-f^{(2M-1)}(a)\Bigr)-\int_a^b\frac{P_{2M}f^{(2M)}}{(2M)!},
$$
the first equality integrating by parts with $P_{2M-2}=P'_{2M-1}/(2M-1)$, whose boundary terms vanish because $P_{2M-1}=B_{2M-1}=0$ at integers when $2M-1\ge3$, and the second with $P_{2M-1}=P'_{2M}/(2M)$, whose boundary terms are $B_{2M}$ at both ends. Hence the display holds for every $M\ge1$, and the bound on $R_M$ is the estimate $\abs{P_{2M}}\le\abs{B_{2M}}$.

:::

:::

::: {.pf-step #log-expansion}

For every integer $M\ge1$ there is a constant $C_M$, independent of $s$, such that
$$
\log\Gamma(s)=\Bigl(s-\frac12\Bigr)\Log s-s+C_M+\sum_{k=1}^{M}c_ks^{1-2k}+O\bigl(\abs{s}^{1-2M}\bigr)
$$
uniformly for $\Re(s)\ge0$ and $\abs{s}\ge1$.

::: pf-proof

The published sentence asserts this display with $\frac12\log(2\pi)$ in place of $C_M$ and with the remainder taken from Problem 1 of Appendix A; the derivation below, through the limit of Exercise 1 of Chapter 6 and the Bernoulli estimate, and the weaker remainder it gives, are the card's own.

Fix $M\ge1$, $\Re(s)>0$ and $n\ge1$, and apply step [](#euler-maclaurin){.pf-ref} on $[0,n]$ to $f(x)=\log(s+x)$, whose derivatives are $f^{(j)}(x)=(-1)^{j-1}(j-1)!/(s+x)^{j}$. Since $\int_0^n\log(s+x)\,dx=(s+n)\log(s+n)-(s+n)-s\Log s+s$ and $(B_{2r}/(2r)!)(2r-2)!=c_r$,
$$
\sum_{k=0}^{n}\log(s+k)=(s+n)\log(s+n)-(s+n)-s\Log s+s+\frac12\Log s+\frac12\log(s+n)+\sum_{r=1}^{M}c_r\Bigl((s+n)^{1-2r}-s^{1-2r}\Bigr)+R_n,
$$
with $R_n=\frac1{2M}\int_0^nP_{2M}(x)(s+x)^{-2M}dx$ and, since $\abs{s+x}\ge(\abs s+x)/\sqrt2$ for $\Re s\ge0$,
$$
\abs{R_n}\le\frac{\abs{B_{2M}}}{2M}\int_0^n\abs{s+x}^{-2M}dx\le\frac{2^M\abs{B_{2M}}}{2M(2M-1)}\abs{s}^{1-2M}.
$$
The same step applied on $[1,n]$ to $g(x)=\log x$, whose derivatives are $g^{(j)}(x)=(-1)^{j-1}(j-1)!/x^{j}$, gives
$$
\log n!=\sum_{k=1}^{n}\log k=n\log n-n+1+\frac12\log n+\sum_{r=1}^{M}c_r\bigl(n^{1-2r}-1\bigr)+R'_n,
\qquad R'_n=\frac1{2M}\int_1^n\frac{P_{2M}(x)}{x^{2M}}\,dx,
$$
and $\abs{R'_n}\le\frac{\abs{B_{2M}}}{2M(2M-1)}$ for every $n$, so $R'_n$ tends to the constant $R'_\infty=\frac1{2M}\int_1^\infty P_{2M}(x)x^{-2M}dx$.

For $\Re(s)>0$, Exercise 1 of Chapter 6 gives $\Gamma(s)=\lim_{n\to\infty}n!\,n^s/\bigl(s(s+1)\cdots(s+n)\bigr)$. For real $s>0$ every factor is positive, so taking logarithms there gives
$$
\log\Gamma(s)=\lim_{n\to\infty}\Bigl(\log n!+s\log n-\sum_{k=0}^{n}\log(s+k)\Bigr)
\tag{$\dagger$}
$$
on $(0,\infty)$, with the real logarithm on the left. Carrying $(\dagger)$ from $(0,\infty)$ to the half-plane is an analytic continuation, not a continuity argument, and runs as follows. Write
$$
L_n(s)\coloneqq\log n!+s\Log n-\sum_{k=0}^{n}\Log(s+k)\qquad(n\ge1),
$$
holomorphic on $\Re(s)>0$ because $\Re(s+k)>0$ there. Its increments are, for $\abs{s/(n+1)}\le\frac12$,
$$
L_{n+1}(s)-L_n(s)=\log(n+1)+s\Log\Bigl(1+\frac1n\Bigr)-\Log(s+n+1)=s\Log\Bigl(1+\frac1n\Bigr)-\Log\Bigl(1+\frac{s}{n+1}\Bigr)=\frac{s}{n(n+1)}+O\Bigl(\frac{\abs{s}^2}{n^2}\Bigr),
$$
the last equality because $\Log(1+w)=w+O(\abs{w}^2)$ for $\abs{w}\le\frac12$; for $\abs{s}\le\rho$ the $O$-constant is uniform once $n+1\ge2\rho$, so $\sum_n\abs{L_{n+1}-L_n}$ converges uniformly on every compact subset of $\Re(s)>0$ and $L\coloneqq\lim_{n\to\infty}L_n$ is holomorphic there. Since $e^{L_n(s)}=n!\,n^s/\bigl(s(s+1)\cdots(s+n)\bigr)$, Exercise 1 of Chapter 6 gives $e^{L(s)}=\Gamma(s)$, so $\Gamma$ has no zeros on $\Re(s)>0$ and $L$ is a branch of $\log\Gamma$ there. The half-plane is simply connected, so a holomorphic branch of $\log\Gamma$ on it exists, and it is unique once its value at one point of $(0,\infty)$ is fixed: any two branches differ by a constant in $2\pi i\ZZ$. Both sides of $(\dagger)$ are therefore holomorphic on $\Re(s)>0$ -- the right side is $L$, the left side the branch of $\log\Gamma$ that is real on $(0,\infty)$ -- and they agree on the open set $(0,\infty)$, where each is the real logarithm, $L$ because every $L_n$ is real there and $e^{L}=\Gamma>0$. Hence by the identity theorem, Corollary 4.9 of Chapter 2, they agree on the whole connected half-plane, which is $(\dagger)$ for $\Re(s)>0$.
Substituting the two displays above and using $(s+n)\log(s+n)=(s+n)\log n+(s+n)\log(1+s/n)$, the terms $n\log n$, $n$ and $s\log n$ cancel, and the bracket equals
$$
-(s+n)\log\Bigl(1+\frac sn\Bigr)+s\Log s+1-\frac12\Log s-\frac12\log\Bigl(1+\frac sn\Bigr)-\sum_{r=1}^{M}c_r+\sum_{r=1}^{M}c_rs^{1-2r}
+\sum_{r=1}^{M}c_rn^{1-2r}-\sum_{r=1}^{M}c_r(s+n)^{1-2r}+R'_n-R_n .
$$
As $n\to\infty$ with $s$ fixed, $(s+n)\log(1+s/n)\to s$, $\log(1+s/n)\to0$, $n^{1-2r}\to0$, $(s+n)^{1-2r}\to0$, $R'_n\to R'_\infty$ and $R_n\to R_\infty(s)\coloneqq\frac1{2M}\int_0^\infty P_{2M}(x)(s+x)^{-2M}dx$. Hence
$$
\log\Gamma(s)=\Bigl(s-\frac12\Bigr)\Log s-s+C_M+\sum_{k=1}^{M}c_ks^{1-2k}-R_\infty(s),
\qquad C_M\coloneqq1-\sum_{k=1}^{M}c_k+R'_\infty,
$$
and $\abs{R_\infty(s)}\le\frac{2^M\abs{B_{2M}}}{2M(2M-1)}\abs{s}^{1-2M}$ by the estimate on $R_n$, uniformly for $\Re(s)\ge0$ and $\abs{s}\ge1$. At $\Re(s)=0$ with $s\ne0$ both sides are continuous, so the identity holds there too.

:::

:::

::: {.pf-step #constant}

$C_M=\frac12\log(2\pi)$, so for every $M\ge1$
$$
\log\Gamma(s)=\Bigl(s-\frac12\Bigr)\Log s-s+\frac12\log(2\pi)+\sum_{k=1}^{M}c_ks^{1-2k}+O\bigl(\abs{s}^{1-2M}\bigr)
$$
uniformly for $\Re(s)\ge0$ and $\abs{s}\ge1$.

::: pf-proof

The published sentence fixes the constant by the Gaussian evaluation in the leading-order Stirling formula; the card carries that out by quoting the leading-order formula itself, Theorem 2.3 of Appendix A, instead of repeating its Gaussian evaluation, and that reduction is the card's own.

Theorem 2.3 of Appendix A states that $\Gamma(s)=e^{s\Log s}e^{-s}\frac{\sqrt{2\pi}}{s^{1/2}}\bigl(1+O(\abs{s}^{-1/2})\bigr)$ as $\abs s\to\infty$ with $s\in S_\delta$, that is,
$$
\log\Gamma(s)=\Bigl(s-\frac12\Bigr)\Log s-s+\frac12\log(2\pi)+O\bigl(\abs{s}^{-1/2}\bigr),
$$
and that theorem is the leading-order Stirling formula, proved there from the Laplace method by the Gaussian evaluation $\int_\RR e^{-x^2}dx=\sqrt\pi$. Subtracting this from step [](#log-expansion){.pf-ref} gives
$$
C_M-\frac12\log(2\pi)=O\bigl(\abs{s}^{-1/2}\bigr)+O\bigl(\abs{s}^{-1}\bigr)
$$
along $s\to+\infty$, whose left-hand side does not depend on $s$; letting $s\to+\infty$ gives $C_M=\frac12\log(2\pi)$.

:::

:::

::: {.pf-step #coefficients}

$c_1=\frac1{12}$, every $c_k$ is rational, hence every $a_j$ is real and $a_1=\frac1{12}$.

::: pf-proof

The claim restates the published sentence; the verification that the coefficients are real is the card's own.

$c_1=\frac{B_2}{2\cdot1}=\frac{1/6}{2}=\frac1{12}$. The Bernoulli numbers are the coefficients of $t/(e^t-1)$, a power series with rational coefficients and nonzero constant term, so every $B_{2k}$, hence every $c_k$, is rational. A power series with real coefficients has a composite with $\exp$ whose Taylor coefficients are real, so $a_j\in\RR$ by the defining display of the preamble; and the coefficient of $u$ in $\exp\bigl(\sum_kc_ku^{2k-1}\bigr)$ is $c_1$, so $a_1=c_1=\frac1{12}$.

:::

:::

::: {.pf-step #right}

For every integer $N\ge1$,
$$
\Gamma(s)=e^{s\Log s-s}\frac{\sqrt{2\pi}}{s^{1/2}}\Bigl(\Psi_N(1/s)+O\bigl(\abs{s}^{-N-1}\bigr)\Bigr)
$$
uniformly for $\Re(s)\ge0$ and $\abs{s}\ge1$.

::: pf-proof

The display is the published expansion; the Taylor estimate that produces it, and the choice of $M$, are the card's own.

Fix $N\ge1$ and choose an integer $M$ with $M\ge N$ and $2M-1\ge N+1$, for instance $M=\max(N,2)$. By steps [](#log-expansion){.pf-ref} and [](#constant){.pf-ref},
$$
\log\Gamma(s)=\Bigl(s-\frac12\Bigr)\Log s-s+\frac12\log(2\pi)+z+O\bigl(\abs{s}^{1-2M}\bigr),
\qquad z\coloneqq\sum_{k=1}^{M}c_ks^{1-2k},
$$
and $\abs z\le C\abs{s}^{-1}\le C$ for $\abs{s}\ge1$, with $C=\sum_{k=1}^{M}\abs{c_k}$. On $\abs z\le C$ the exponential is bounded by $e^{C}$ and its Taylor polynomial of degree $N$ approximates it to within $e^C\abs z^{N+1}/(N+1)!$, so
$$
e^{z}=\sum_{j=0}^{N}\frac{z^{j}}{j!}+O\bigl(\abs{s}^{-N-1}\bigr)=\Psi_N(1/s)+O\bigl(\abs{s}^{-N-1}\bigr),
$$
the last step because $z$ differs from $\sum_{k=1}^{N}c_ks^{1-2k}$ by $O(\abs{s}^{-2N-1})$, and $\sum_{j\le N}z^j/j!$ has the Taylor polynomial $\Psi_N(1/s)$ of $\exp\bigl(\sum_{k\le N}c_ku^{2k-1}\bigr)$ as its part of degree $\le N$ in $u=1/s$. Exponentiating the display for $\log\Gamma$ and using $e^{O(\abs{s}^{1-2M})}=1+O(\abs{s}^{1-2M})$ together with $1-2M\le-N-1$,
$$
\Gamma(s)=e^{(s-\frac12)\Log s}e^{-s}e^{\frac12\log(2\pi)}e^{z}\bigl(1+O(\abs{s}^{-N-1})\bigr)
=e^{s\Log s-s}\frac{\sqrt{2\pi}}{s^{1/2}}\Bigl(\Psi_N(1/s)+O\bigl(\abs{s}^{-N-1}\bigr)\Bigr),
$$
since $e^{(s-\frac12)\Log s}=e^{s\Log s}s^{-1/2}$ and $e^{\frac12\log(2\pi)}=\sqrt{2\pi}$.

:::

:::

::: {.pf-step #reflection}
For all $s$ in the slit plane,
$$
F(s)F(-s)=\frac{1}{1-e^{2\pi is}}\ \text{ if }\ \Im(s)>0,
\qquad
F(s)F(-s)=\frac{1}{1-e^{-2\pi is}}\ \text{ if }\ \Im(s)<0 .
$$

::: pf-proof
This step is the card's own: the published solution folds the passage to the whole sector into the words "in the fixed sector", and the book's proof of Theorem 2.3 of Appendix A takes it by the same two identities, which it cites as Theorem 1.4 and Lemma 1.2 of Chapter 6.

By Theorem 1.4 of Chapter 6 and Lemma 1.2 of Chapter 6, $\Gamma(s)\Gamma(1-s)=\pi/\sin\pi s$ and $\Gamma(1-s)=-s\Gamma(-s)$, hence
$$
\Gamma(s)\Gamma(-s)=\frac{\pi}{-s\sin\pi s},
\tag{$\ast$}
$$
which is the reflection formula in the form used below. Assume first that $\Im(s)>0$, so that $\theta=\arg s\in(0,\pi)$; then $-s$ has argument $\theta-\pi\in(-\pi,0)$, and therefore
$$
\log(-s)=\log s-i\pi,\qquad (-s)^{1/2}=s^{1/2}e^{-i\pi/2}=-i\,s^{1/2}.
$$
Using these and $(\ast)$,
$$
F(s)F(-s)=\frac{\Gamma(s)\Gamma(-s)}{2\pi}\,s^{1/2}(-s)^{1/2}\,e^{-s\log s+s+s\log(-s)-s}
=\frac{-\pi}{2\pi s\sin\pi s}\,(-i)s\,e^{-i\pi s}
=\frac{i\,e^{-i\pi s}}{2\sin\pi s},
$$
and $2\sin\pi s=(e^{i\pi s}-e^{-i\pi s})/i$ gives $\frac{ie^{-i\pi s}}{2\sin\pi s}=-\frac{e^{-i\pi s}}{e^{i\pi s}-e^{-i\pi s}}=-\frac{1}{e^{2\pi is}-1}=\frac{1}{1-e^{2\pi is}}$. For $\Im(s)<0$ apply the result just proved to $\overline s$ (which has positive imaginary part) and conjugate, using $\overline{F(s)}=F(\overline{s})$ (the principal branches of $\log$ and of the square root are symmetric) and $\overline{1/(1-e^{2\pi i\overline s})}=1/(1-e^{-2\pi is})$; this gives the second identity. Both identities can also be read off from the single meromorphic identity obtained by continuing the first one across the real axis, which multiplies $1-e^{2\pi is}$ by no factor but replaces $F(-s)$ by the continuation of $F$ past the cut, which is why the two cases differ.

:::

:::

::: {.pf-step #left}
For every integer $N\ge1$ there is a constant $R_N\ge4+2A_N$, depending only on $N$, such that for $s\in S_\delta$ with $\Re(s)<0$ and $\abs{s}\ge R_N$,
$$
F(s)=\frac{1}{\Psi_N(-1/s)}+O\bigl(\abs{s}^{-N-1}\bigr),
$$
uniformly on $\{s\in S_\delta:\Re(s)\le0,\ \abs{s}\ge R_N\}$.

::: pf-proof
This step is the card's own. The published solution asserts the expansion on the whole sector in one sentence -- "Apply the Euler--Maclaurin formula to $\log\Gamma(s)$ in the fixed sector $S_\delta$" -- and says nothing about the reciprocal of $\Psi_N$; both the passage to the half-plane $\Re(s)<0$ and the lower bound that the reciprocal needs are supplied here.

Choose $R_N\ge4+2A_N$ so large that the estimate of step [](#right){.pf-ref} applied at $-s$ gives
$$
\abs{F(-s)-\Psi_N(-1/s)}\le\frac14\qquad\text{for}\qquad \Re(s)\le0,\ \abs{s}\ge R_N ;
$$
such an $R_N$ exists, and depends on $N$ alone, because that remainder is $O(\abs{s}^{-N-1})$ uniformly on $\Re(-s)\ge0$ with $\abs{s}\ge1$. Let $s$ lie in the set of the claim and put $u\coloneqq-1/s$, so that $\abs{u}=1/\abs{s}\le1/(4+2A_N)\le1/(2A_N)$; the preamble's bound then gives $\abs{\Psi_N(u)-1}\le A_N\abs{u}\le\frac12$, the number $A_N$ being at least $\abs{a_1}=\frac1{12}>0$ by step [](#coefficients){.pf-ref}. Hence
$$
\abs{\Psi_N(-1/s)}\ge\frac12,\qquad\text{and}\qquad\abs{F(-s)}\ge\abs{\Psi_N(-1/s)}-\abs{F(-s)-\Psi_N(-1/s)}\ge\frac14 .
$$
Both bounds hold uniformly on the whole set, so the reciprocal below needs no separate argument at infinity and none on a compact remainder, and nothing about $\Psi_N$ is inferred from continuity or from the non-vanishing of $F$. Hence
$$
\frac{1}{F(-s)}=\frac{1}{\Psi_N(-1/s)}+O\bigl(\abs{s}^{-N-1}\bigr),
$$
the difference of the two sides being $(F(-s)-\Psi_N(-1/s))/\bigl(F(-s)\Psi_N(-1/s)\bigr)$, whose modulus is at most $8\abs{F(-s)-\Psi_N(-1/s)}$.

By step [](#reflection){.pf-ref}, $F(s)=1/\bigl(\varepsilon(s)F(-s)\bigr)$ with $\varepsilon(s)=1-e^{2\pi is}$ if $\Im(s)>0$ and $\varepsilon(s)=1-e^{-2\pi is}$ if $\Im(s)<0$. In both cases $\abs{e^{\mp2\pi is}}=e^{-2\pi\abs{\Im s}}$, and $\abs{\Im s}=\abs{s}\abs{\sin(\arg s)}\ge\abs{s}\sin\delta$ for $s\in S_\delta$ because $\abs{\arg s}\le\pi-\delta$; thus $e^{-2\pi\abs{\Im s}}\le e^{-2\pi\abs{s}\sin\delta}\le c_\delta<1$ for $\abs{s}\ge4$, so $\abs{1/\varepsilon(s)}\le1/(1-c_\delta)$ and $1/\varepsilon(s)=1+O(e^{-2\pi\abs{\Im s}})=1+O(\abs{s}^{-N-1})$ for every $N$. Multiplying the two estimates gives $F(s)=1/\Psi_N(-1/s)+O(\abs{s}^{-N-1})$.

:::

:::

::: {.pf-step #identify}
$\Psi_N(u)\Psi_N(-u)=1+O\bigl(\abs{u}^{N+1}\bigr)$ as $u\to0$, and consequently
$$
F(s)=\Psi_N(1/s)+O\bigl(\abs{s}^{-N-1}\bigr)\qquad\text{for } s\in S_\delta,\ \Re(s)<0,\ \abs{s}\ge R_N ,
$$
with $R_N$ the constant of step [](#left){.pf-ref}.

::: pf-proof
This step is the card's own. If $\delta>\pi/2$ then $S_\delta\subset\{\Re(s)>0\}$ and there is nothing to prove, so assume $\delta\le\pi/2$; then the imaginary axis lies in $S_\delta$, and every $it$ with $t\ge R_N$ belongs to the sets on which the estimates of steps [](#right){.pf-ref} and [](#left){.pf-ref} are uniform.
Let $t\ge R_N$ and put $s=it$. By step [](#right){.pf-ref}, $F(it)=\Psi_N(1/(it))+O(t^{-N-1})=\Psi_N(-i/t)+O(t^{-N-1})$. On the other hand, $\Re(s)\le0$ and the estimates of step [](#left){.pf-ref} are uniform on that set; taking the limit of the identity of step [](#left){.pf-ref} along $s\to it$ with $\Re(s)<0$ (both sides being continuous at $it\ne0$) gives $F(it)=1/\Psi_N(-1/(it))+O(t^{-N-1})=1/\Psi_N(i/t)+O(t^{-N-1})$.
Subtracting, $\Psi_N(-i/t)-1/\Psi_N(i/t)=O(t^{-N-1})$. Write $1/\Psi_N(u)=\sum_{j=0}^{N}b_ju^{j}+O(u^{N+1})$ for $\abs{u}\le1/2$, which exists because $\Psi_N(0)=1$; then $1/\Psi_N(i/t)=\sum_{j=0}^{N}b_ji^{j}t^{-j}+O(t^{-N-1})$ and $\Psi_N(-i/t)=\sum_{j=0}^{N}a_j(-i)^{j}t^{-j}+O(t^{-N-1})$, so
$$
\sum_{j=0}^{N}\bigl(a_j(-i)^{j}-b_ji^{j}\bigr)t^{-j}=O(t^{-N-1}).
$$
Put $u=1/t$ and $c_j\coloneqq a_j(-i)^{j}-b_ji^{j}$; the display reads $\sum_{j=0}^{N}c_ju^{j}=O(u^{N+1})$ as $u\to0$. Multiplying by $t^{n}$ does not isolate $c_n$, because the terms of index $j<n$ then grow without bound; the coefficients are recovered instead by induction on $n$. For $n=0$ the display gives $c_0=O(u)$, hence $c_0=0$. If $c_0=\cdots=c_{n-1}=0$ for some $n\le N$, then $\sum_{j=0}^{n}c_ju^{j}=c_nu^{n}+O(u^{n+1})=O(u^{n+1})$; dividing by $u^{n}$ and letting $u\to0$ gives $c_n=0$. Hence $a_n(-i)^{n}=b_ni^{n}$, that is $b_n=(-1)^{n}a_n$, for every $n\le N$; hence $1/\Psi_N(u)=\Psi_N(-u)+O(u^{N+1})$, and multiplying by $\Psi_N(u)$ yields $\Psi_N(u)\Psi_N(-u)=1+O(\abs{u}^{N+1})$.
Substituting this into step [](#left){.pf-ref}, with $u=-1/s$, gives $1/\Psi_N(-1/s)=\Psi_N(1/s)+O(\abs{s}^{-N-1})$, which proves the second assertion.

:::

:::

::: pf-qed
The display is the published expansion; the half of the sector with $\Re(s)<0$, which the case below takes from step [](#identify){.pf-ref}, is the card's own.

Let $N\ge1$ and let $\abs{s}\ge R_N$ with $s\in S_\delta$, the constant $R_N$ being that of step [](#left){.pf-ref}. If $\Re(s)\ge0$, step [](#right){.pf-ref} gives $\Gamma(s)=e^{s\log s}e^{-s}\frac{\sqrt{2\pi}}{s^{1/2}}\bigl(1+\sum_{j=1}^{N}a_js^{-j}+O(s^{-N})\bigr)$; if $\Re(s)<0$, step [](#identify){.pf-ref} gives the same, since $F(s)=\Psi_N(1/s)+O(\abs{s}^{-N-1})$ translates into exactly that display. The constants $a_j$ are real and $a_1=1/12$ by step [](#coefficients){.pf-ref}. As for every $N>0$ one may take the integer $N$ above replaced by $\lceil N\rceil$, this is the assertion of the problem.

:::

:::

:::
