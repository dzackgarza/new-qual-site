---
schema: qual/card@1
id: E-SSA.PR-1
kind: problem
title: Watson's lemma for a truncated integral with a smooth cutoff
classification:
  areas:
  - complex-analysis
  topics:
  - Asymptotics
  - Laplace Transform
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 1,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Solution installed following the book's own strategy: the cutoff lemma by n integrations by parts with vanishing boundary terms, uniform for Re s >= 0, giving (a); and (b) by reducing to the case m-k in (-1,0] and then k integrations by parts whose boundary terms vanish because m-k+1 > 0, with the Gamma factors identified through Gamma(m+1) = (m-k)! Gamma(m-k+1).
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read again while the corpus style rules were swept over this residue: the absolute value in the
    closing step named its own delimiters with explicit sizing commands instead of `\abs{...}`, which
    STYLE-04 asks for, and it is now `\abs{...}`. Nothing inside the absolute value, and nothing in
    the bound beside it, changed. Checked in this pass: that the closing step's formula is the one
    the two claims above it give, and that `\abs` is already the card's notation for a modulus in
    the same display. Not checked in this pass: the argument of either claim, which this edit does
    not touch.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the appendix section, the problem number, the file and
    the printed pages. The card's 2026-11-01 event had already recorded the reading (Appendix A, §5,
    problem 1, PDF pp. 359-363, printed pp. 341-343); this event only moves that locator into the
    rendered text, where a reader sees it, and the page range was re-confirmed at PDF p. 360, whose
    running head is printed p. 341 under the heading "5. Problems". No mathematics changed.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Locator correction to the events above: Appendix A's Problems occupy PDF pp. 360--362 of the
    retained scan, printed pp. 341--343, not PDF pp. 359--363; PDF p. 359 is printed p. 340 and
    PDF p. 363 is the Appendix B title page. This item was not otherwise re-read in this pass, and it
    carries no asterisk -- the print's Appendix A mark is before Problem 5 only.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Citation corrected on the reader's report. The solution's opening sentence cited Chapter 6,
    Lemma 1.2 for $\Gamma(m+1)=\int_0^\infty e^{-t}t^m\,dt$; that lemma states the recursion
    $\Gamma(s+1)=s\Gamma(s)$ and its consequence $\Gamma(n+1)=n!$, and carries no integral. Read
    again in the retained book, the integral formula is Chapter 6, equation (1),
    $\Gamma(s)=\int_0^\infty e^{-t}t^{s-1}\,dt$ for $s>0$, at $s=m+1$, together with Chapter 6,
    Proposition 1.1, which states that $\Gamma$ extends analytically to $\Re(s)>0$ and is still given
    there by the integral formula (1). The citation now names those two. The citation of Lemma 1.2
    inside the final step stands: that step applies the recursion, which is what the lemma states.
    The mathematics of the argument is unchanged and was not re-read in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Chapter named in a second citation of the same solution: the sentence that identifies the
    substitution of the step with "the computation (5) of Proposition 1.2" named no chapter, and
    Chapter 6 has no Proposition 1.2 -- its numbered statements are Proposition 1.1, Lemma 1.2,
    Theorem 1.3, Theorem 1.4, Lemma 1.5, Theorem 1.6 and Theorem 1.7. Read in the retained book, the
    statement meant is Appendix A, Proposition 1.2, whose equation (5) is the truncated integral
    $\int_0^a e^{-sx}x^m\,dx=s^{-m-1}\Gamma(m+1)+O(e^{-cs})$; the sentence now names Appendix A.
    Nothing else changed.
---

::: {.exercise}
Let $\eta$ be an indefinitely differentiable function supported in a finite interval, so that $\eta(x)=1$ for $x$ near $0$. Then, if $m>-1$ and $N>0$,
$$
\int_0^\infty e^{-sx}x^m\eta(x)\,dx=s^{-m-1}\Gamma(m+1)+O(s^{-N})
$$
for $\operatorname{Re}(s)\ge0$, $\abs{s}\to\infty$.

(a) Consider first the case $-1<m\le0$. It suffices to see that
$$
\int_0^\infty e^{-sx}x^m(1-\eta(x))\,dx=O(s^{-N}),
$$
and this can be done by repeated integration by parts since $e^{-sx}=(-1)^Ns^{-N}\bigl(\tfrac{d}{dx}\bigr)^N(e^{-sx})$.

(b) To extend this to all $m$, find an integer $k$ so that $k-1<m\le k$, write
$$
\int_0^\infty\Bigl(\frac{d}{dx}\Bigr)^k\bigl(x^m\bigr)e^{-sx}\eta(x)\,dx=c_{k,m}s^{-m+k-1}+O(s^{-N}),
$$
and integrate by parts $k$ times.
:::

::: {.remark}
Appendix A sets its asterisk before Problem 5 only, so none stands before this problem (Appendix A, Problem 1).
:::

::: {.solution}
This is Problem 1 of Section 5 of Appendix A of Stein and Shakarchi, *Complex Analysis*, retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`; the statement below is its wording.
Throughout, $\eta\in C^\infty(\RR)$ is supported in a finite interval $[-b,b]$ with $b>0$, and $\eta=1$ on $(-a,a)$ for some $0<a\le b$; put $\chi=1-\eta$, so that $\chi\equiv 0$ on $(-a,a)$ and $\chi\equiv 1$ on $(b,\infty)$. We write $s^{-m-1}$ for the branch of the power on $\CC\setminus(-\infty,0]$ that is positive on $(0,\infty)$, and $\Gamma$ for Euler's gamma function, so that $\Gamma(m+1)=\int_0^\infty e^{-t}t^m\,dt$ for $m>-1$ (Chapter 6, equation (1) and Proposition 1.1). Since $N>0$ is arbitrary, it suffices to prove, for each integer $n\ge 1$, the estimate $O(\abs{s}^{-n})$ with a constant depending only on $m$, $n$ and $\eta$; the assertion for a given $N$ then follows with $n=\max(1,\lceil N\rceil)$. All estimates below are uniform for $\Re(s)\ge 0$ and $\abs{s}\ge 1$, and $s\ne 0$.

::: pf

::: {.pf-step #cutoff}
Let $g\in C^\infty([0,\infty))$ vanish identically on $[0,a)$ and on $(b,\infty)$. Then for every integer $n\ge 0$ and every $s\neq 0$ with $\Re(s)\ge 0$,
$$
\abs{\int_0^\infty e^{-sx}g(x)\,dx}\ \le\ \abs{s}^{-n}\int_0^b\abs{g^{(n)}(x)}\,dx .
$$

::: pf-proof
Since $g$ is supported in $[0,b]$, the integral equals $\int_0^b e^{-sx}g(x)\,dx$. Because $g$ vanishes identically on a neighbourhood of $0$ and of $b$, every derivative $g^{(k)}$ vanishes at $x=0$ and at $x=b$. Since $e^{-sx}=-\frac1s\frac{d}{dx}\bigl(e^{-sx}\bigr)$, an integration by parts gives
$$
\int_0^b e^{-sx}g(x)\,dx=\Bigl[-\frac{e^{-sx}}{s}g(x)\Bigr]_0^b+\frac1s\int_0^b e^{-sx}g'(x)\,dx=\frac1s\int_0^b e^{-sx}g'(x)\,dx,
$$
the boundary term being zero. Iterating this $n$ times, again with all boundary terms zero, gives $\int_0^b e^{-sx}g(x)\,dx=(-1)^n s^{-n}\int_0^b e^{-sx}g^{(n)}(x)\,dx$. Since $\abs{e^{-sx}}=e^{-\Re(s)x}\le 1$ for $x\ge 0$ and $\Re(s)\ge 0$, the estimate follows.

:::

:::

::: {.pf-step #parta}
For $-1<m\le 0$ and every integer $n\ge 1$,
$$
\int_0^\infty e^{-sx}x^m\eta(x)\,dx=s^{-m-1}\Gamma(m+1)+O\bigl(\abs{s}^{-n}\bigr).
$$

::: pf-proof
For $\Re(s)>0$ the substitution $x=t/s$ (a change of variables along the ray $\{t/s:t>0\}$, both integrals being absolutely convergent because $m>-1$ and $\Re(s)>0$) gives the identity
$$
\int_0^\infty e^{-sx}x^m\,dx=s^{-m-1}\int_0^\infty e^{-t}t^m\,dt=s^{-m-1}\Gamma(m+1),
\tag{1}
$$
which is also the computation (5) of Proposition 1.2 of Appendix A.
Define
$$
D(s)=\int_0^\infty e^{-sx}x^m\eta(x)\,dx-s^{-m-1}\Gamma(m+1),\qquad T(s)=\int_0^\infty e^{-sx}x^m\chi(x)\,dx .
$$
By (1) and $\eta=1-\chi$ we have $D(s)=-T(s)$ for $\Re(s)>0$. The function $s\mapsto\int_0^\infty e^{-sx}x^m\eta(x)\,dx$ is entire, because $\eta$ is supported in $[0,b]$ and $x^m$ is integrable on $[0,b]$; the function $s\mapsto s^{-m-1}\Gamma(m+1)$ is holomorphic on the slit plane $\CC\setminus(-\infty,0]$, on which the principal branch of the power is defined; and $T$ is entire. Hence $D$ and $-T$ are both holomorphic on the slit plane and they agree on the non-empty open set $\{\Re(s)>0\}$, so by the identity theorem $D=-T$ on the whole slit plane. Since $\{\Re(s)\ge 0\}\setminus\{0\}$ lies in the slit plane, it remains to bound $T$.

The function $g_m(x)=x^m\chi(x)$, extended by $0$ for $x\le 0$, lies in $C^\infty([0,\infty))$: on $(0,\infty)$ it is a product of smooth functions, and on $[0,a)$ it vanishes identically, so all its derivatives vanish there. Its support is contained in $[0,b]$, and it vanishes identically on $[0,a)$. So step [](#cutoff){.pf-ref} gives, for every $n\ge 1$,
$$
\abs{T(s)}=\abs{\int_0^\infty e^{-sx}g_m(x)\,dx}\le\abs{s}^{-n}\int_0^b\abs{g_m^{(n)}(x)}\,dx ,
$$
and $\int_0^b\abs{g_m^{(n)}}$ is finite because $g_m\in C^\infty$ has compact support. Hence $\abs{D(s)}=\abs{T(s)}=O(\abs{s}^{-n})$.

:::

:::

::: {.pf-step #choose-k}
Let $m>-1$ and let $k\ge 0$ be the integer with $k-1<m\le k$. Then $-1<m-k\le 0$ and, with $c=\prod_{j=0}^{k-1}(m-j)$ (the empty product for $k=0$),
$$
\Bigl(\frac{d}{dx}\Bigr)^k\bigl(x^m\bigr)=c\,x^{m-k}\quad\text{for } x>0,
\qquad c\neq 0 .
$$
Moreover $k=0$ exactly when $-1<m\le0$.

::: pf-proof
The integer $k\ge0$ with $k-1<m\le k$ exists by the Archimedean property of $\RR$, and $k=0$ means $-1<m\le0$ while $k\ge1$ means $k-1<m$, i.e. $m>k-1\ge0$. Thus $k-1<m$ gives $m-k>-1$ and $m\le k$ gives $m-k\le0$. Differentiating the monomial $k$ times gives $\bigl(x^m\bigr)^{(k)}=m(m-1)\cdots(m-k+1)x^{m-k}=c\,x^{m-k}$ (for $k=0$ both sides are $x^m$). Every factor $m-j$ with $0\le j\le k-1$ is nonzero: when $k\ge1$ we have $m-j\ge m-k+1>0$. Hence $c\neq0$.

:::

:::

::: {.pf-step #reduced}
With $k\ge0$ and $c$ as in step [](#choose-k){.pf-ref}, and every integer $n\ge1$,
$$
\int_0^\infty e^{-sx}\Bigl(\frac{d}{dx}\Bigr)^k\bigl(x^m\bigr)\eta(x)\,dx=c\,\Gamma(m-k+1)\,s^{-m+k-1}+O\bigl(\abs{s}^{-n}\bigr).
$$

::: pf-proof
By step [](#choose-k){.pf-ref} the integrand is $c\,e^{-sx}x^{m-k}\eta(x)$, and $m-k\in(-1,0]$. Step [](#parta){.pf-ref} applies to the exponent $m-k$ and gives $\int_0^\infty e^{-sx}x^{m-k}\eta(x)\,dx=s^{-(m-k)-1}\Gamma(m-k+1)+O(\abs{s}^{-n})=s^{-m+k-1}\Gamma(m-k+1)+O(\abs{s}^{-n})$; multiplying by $c$ gives the claim. (For $k=0$ this is step [](#parta){.pf-ref} itself.)

:::

:::

::: {.pf-step #ibp}
Fix $s\neq0$ and, for $0\le i\le k$, set
$$
F_i=\int_0^\infty e^{-sx}\bigl(x^m\bigr)^{(i)}(x)\,\eta(x)\,dx,
\qquad
G_i=\int_0^\infty e^{-sx}\bigl(x^m\bigr)^{(i)}(x)\,\eta'(x)\,dx .
$$
All these integrals converge absolutely. Moreover
$$
F_k=s^kF_0-\sum_{i=0}^{k-1}s^{k-1-i}G_i,
\qquad\text{and}\qquad G_i=O\bigl(\abs{s}^{-n}\bigr)\ \text{for every } n\ge 0 .
$$

::: pf-proof
That the $F_i$ converge follows from $\bigl(x^m\bigr)^{(i)}=c_i x^{m-i}$ with $m-i\ge m-k>-1$ and $\eta$ supported in $[0,b]$; the $G_i$ converge because $\eta'$ is supported in $[a,b]$ and $x^{m-i}$ is bounded there when $m-i\ge 0$, and integrable there when $m-i<0$. (For $k=0$ the assertions are $F_0=F_0$ and, for each $i$, the $G_i$ estimate below.)

For $1\le i\le k$ integrate by parts with $u=e^{-sx}\eta(x)$, $v=\bigl(x^m\bigr)^{(i-1)}$, so that $du=\bigl(-se^{-sx}\eta(x)+e^{-sx}\eta'(x)\bigr)dx$. Since $\eta$ vanishes identically on $(b,\infty)$ and $\bigl(x^m\bigr)^{(i-1)}=c_{i-1}x^{m-i+1}$ with $m-i+1\ge m-k+1>0$, the boundary term $\bigl[e^{-sx}\eta(x)\bigl(x^m\bigr)^{(i-1)}(x)\bigr]_0^\infty$ vanishes: at $x\to\infty$ because $\eta$ is eventually $0$, and at $x=0$ because $x^{m-i+1}\to0$. Hence
$$
F_i=sF_{i-1}-G_{i-1}\qquad(1\le i\le k).
$$
Iterating this relation gives $F_k=s^kF_0-\sum_{i=0}^{k-1}s^{k-1-i}G_i$: indeed, for $k=1$ it is the relation itself, and for $k>1$ we have $F_k=sF_{k-1}-G_{k-1}=s\bigl(s^{k-1}F_0-\sum_{i=0}^{k-2}s^{k-2-i}G_i\bigr)-G_{k-1}=s^kF_0-\sum_{i=0}^{k-1}s^{k-1-i}G_i$.

Finally, fix $i$ and put $g_i=\bigl(x^m\bigr)^{(i)}\eta'$. Since $\eta'$ vanishes identically on $[0,a)$ and on $(b,\infty)$, and $x^{m-i}$ is smooth on $(0,\infty)$, the function $g_i$, extended by $0$ outside $[a,b]$, lies in $C^\infty([0,\infty))$, is supported in $[0,b]$ and vanishes identically on $[0,a)$. So step [](#cutoff){.pf-ref} gives $\abs{G_i}\le\abs{s}^{-n}\int_0^b\abs{g_i^{(n)}}$, and the integral is finite. This holds for every $n\ge0$.

:::

:::

::: {.pf-step #partb}
For every $m>-1$ and every integer $n\ge 1$,
$$
\int_0^\infty e^{-sx}x^m\eta(x)\,dx=s^{-m-1}\Gamma(m+1)+O\bigl(\abs{s}^{-n}\bigr).
$$

::: pf-proof
Fix $m>-1$ and $k$, $c$ as in step [](#choose-k){.pf-ref}. Step [](#ibp){.pf-ref} gives $F_0=s^{-k}\bigl(F_k+\sum_{i=0}^{k-1}s^{k-1-i}G_i\bigr)=s^{-k}F_k+O\bigl(\abs{s}^{-n-1}\bigr)$, because $s^{-k}s^{k-1-i}=s^{-1-i}$ and $\abs{s}\ge1$. Substituting the expansion of $F_k$ from step [](#reduced){.pf-ref},
$$
F_0=s^{-k}\bigl(c\,\Gamma(m-k+1)s^{-m+k-1}+O(\abs{s}^{-n})\bigr)+O\bigl(\abs{s}^{-n-1}\bigr)
=c\,\Gamma(m-k+1)s^{-m-1}+O\bigl(\abs{s}^{-n}\bigr).
$$
By Lemma 1.2 of Chapter 6, $\Gamma(w+1)=w\Gamma(w)$; applied $k$ times, with all arguments $m-k+1,\dots,m$ lying in $\{\Re(w)>0\}$ because $m-k+1>0$, it gives $\Gamma(m+1)=m(m-1)\cdots(m-k+1)\Gamma(m-k+1)=c\,\Gamma(m-k+1)$. This proves the claim.

:::

:::

::: pf-qed
Step [](#parta){.pf-ref} proves assertion (a) of the problem, and step [](#partb){.pf-ref} proves assertion (b). Together they give, for every $m>-1$, every integer $n\ge1$ and all $s$ with $\Re(s)\ge0$, $\abs{s}\ge1$,
$$
\abs{\int_0^\infty e^{-sx}x^m\eta(x)\,dx-s^{-m-1}\Gamma(m+1)}\le C_{m,n,\eta}\abs{s}^{-n},
$$
and choosing $n=\max(1,\lceil N\rceil)$ for the given $N>0$ yields $\int_0^\infty e^{-sx}x^m\eta(x)\,dx=s^{-m-1}\Gamma(m+1)+O(s^{-N})$ as $\abs{s}\to\infty$ in the closed half-plane $\Re(s)\ge0$, as required.

:::

:::

:::
