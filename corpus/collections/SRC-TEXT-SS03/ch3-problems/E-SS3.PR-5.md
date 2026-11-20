---
schema: qual/card@1
id: E-SS3.PR-5
kind: problem
title: The Cauchy integral of a function on an interval, and its jump
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral
  - Boundary Behaviour
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Chapter 3, §9, problem 5, read from
    `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF page 129). This card did not
    exist before: it was found missing by a completeness audit of the collection against the book,
    which located every printed Exercises and Problems item and compared it with the cards on disk.
    The transcription was taken from the OCR text layer and cleaned of OCR errors; the asterisk marking a starred problem, and the
    printed wording, hypotheses and bracketed hints are preserved.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Solution installed from a source-verified pass. Two corrections to the printed statement are proved rather than asserted: the jump identity holds on the open interval and gives h(+-M)/2 at the endpoints, and the uniform convergence claimed in (b) fails when h(+-M) != 0, since |g(M+i eps)| = (|h(M)|/2 pi) log(1/eps) + O(1). The characterisation is unique as stated on the closed interval.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps without altering the mathematics: the two lemmas, Steps 1 to 6
    and the endpoint discussion are now numbered steps, each carrying the prose that was already on
    the card as its proof, and the four remarks on the printed statement follow the proof block as
    the card had them. Checked while restructuring: the Poisson kernel normalisation and its tail
    estimate; the holomorphy of g from the parametrised integral over [0,1] and Theorem 5.4 of
    Chapter 2; the vanishing at infinity from |y - z| >= |z|/2 for |z| >= 2M; the jump identity from
    the difference of the two kernels equalling 2 i epsilon/((y-x)^2 + epsilon^2), which is
    2 pi P_epsilon(y - x); the endpoint value h(+-M)/2 from half of the kernel's mass falling
    outside [-M, M]; the Plemelj formula with the three estimates (existence of A, B_epsilon ->
    pi h, A_epsilon -> A); the uniform version when h(+-M) = 0 using the extension H and Lemma 2;
    and the characterisation, both uniqueness (symmetry principle, maximum modulus, removable
    singularity, Liouville) and the failure when h(M) != 0 (logarithmic growth). The card's two
    recorded corrections to the printed statement (the jump identity on the open interval, and the
    endpoint hypothesis needed for uniformity) are retained in the remarks. Statement unchanged; the
    card does not claim a retained solution set covers this problem.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Provenance sentence added to the solution's opening, which the per-card rule requires and the
    card lacked. Checked before writing it: the checkout's sources for Stein-Shakarchi are the book
    itself (assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf and its page extractions), and
    no solution set for the book is present under tmp/sources or assets/attachments; the Hartshorne
    solution file that carries Stein's name is a different book's solutions. No search outside the
    checkout was made for this step, and no page of a solution set was read. The mathematics of the
    card is unchanged.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    The asterisk the print sets before "5." was read from the page image of printed p. 110 (PDF
    p. 129), which is also the locator the first event gives, so that locator is right. The two
    recorded corrections to the printed statement were re-checked and hold: the jump limit at
    $x=\pm M$ is $h(\pm M)/2$, half the Poisson mass falling outside $[-M,M]$, and the uniform
    convergence of (b) does fail at the endpoints when $h(\pm M)\ne0$, since
    $\int_{-M}^{M}dx/(x-M-i\epsilon)=-\log(1/\epsilon)+O(1)$ makes
    $\abs{g(M+i\epsilon)}=\frac{\abs{h(M)}}{2\pi}\log(1/\epsilon)+O(1)$. Not checked: the
    Plemelj estimates and the uniqueness argument were read for sense but not re-derived today.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Repair of step s5 on the reader's report. It concluded "in particular $g$ is bounded on
    $\Omega$" from $g(z)\to0$ at infinity, which does not follow: the estimate proves boundedness only
    on $\Omega\cap\{\abs z\ge2M\}$, and step s11 exhibits logarithmic divergence of
    $g(M+i\varepsilon)$ when $h(M)\ne0$. The clause now states the boundedness it proves, namely
    $\abs{g(z)}\le B/\pi$ for $\abs z\ge2M$, and names step s11 as the reason the whole of $\Omega$ is
    not claimed. No other step changed. Provenance: a search outside the checkout was made for this
    pass and changed the provenance sentence of 2026-11-19 — Rhoades, *Solutions/Hints to the
    Exercises from Complex Analysis by Stein and Shakarchi* (2006), covers a selection of the
    Exercises and not the end-of-chapter Problems, so no published solution of this Problem was
    located.
---

::: {.exercise}
Let
$$
g(z)=\frac{1}{2\pi i}\int_{-M}^{M}\frac{h(x)}{x-z}\,dx
$$
where $h$ is continuous and supported in $[-M,M]$.

(a) Prove that the function $g$ is holomorphic in $\CC\setminus[-M,M]$, and vanishes at infinity, that is, $\lim_{\abs z\to\infty}\abs{g(z)}=0$. Moreover, the "jump" of $g$ across $[-M,M]$ is $h$, that is,
$$
h(x)=\lim_{\epsilon\to0,\ \epsilon>0}g(x+i\epsilon)-g(x-i\epsilon).
$$
[Hint: Express the difference $g(x+i\epsilon)-g(x-i\epsilon)$ in terms of a convolution of $h$ with the Poisson kernel.]

(b) If $h$ satisfies a mild smoothness condition, for instance a H\"older condition with exponent $\alpha$, that is, $\abs{h(x)-h(y)}\le C\abs{x-y}^{\alpha}$ for some $C>0$ and all $x,y\in[-M,M]$, then $g(x+i\epsilon)$ and $g(x-i\epsilon)$ converge uniformly to functions $g^+(x)$ and $g^-(x)$ as $\epsilon\to0$. Then $g$ can be characterized as the unique holomorphic function that satisfies:

(i) $g$ is holomorphic outside $[-M,M]$,

(ii) $g$ vanishes at infinity,

(iii) $g(x+i\epsilon)$ and $g(x-i\epsilon)$ converge uniformly as $\epsilon\to0$ to functions $g^+(x)$ and $g^-(x)$ with
$$
g^+(x)-g^-(x)=h(x).
$$
[Hint: If $G$ is another function satisfying these conditions, $g-G$ is entire.]
:::

::: {.remark}
The book marks this problem with an asterisk (Chapter 3, Problem 5).
:::

::: {.solution}
Let $M>0$, let $h\colon[-M,M]\to\CC$ be continuous, put $B\coloneqq\sup_{[-M,M]}\abs{h}$, and set

$$
g(z)\coloneqq\frac{1}{2\pi i}\int_{-M}^{M}\frac{h(y)}{y-z}\,dy,\qquad z\in\Omega\coloneqq\CC\setminus[-M,M].
$$

The only results of the book used below are Theorem 5.4, Theorem 5.5 and Corollary 4.5 of Chapter 2, and Theorem 3.1 and Corollary 4.6 of Chapter 3 [@SS03]. The two elementary lemmas they are applied through are proved first. Nothing about the behaviour of $h$ at the endpoints $\pm M$ is assumed unless it is stated. The argument is this card's own: no retained solution set in the checkout covers the problems of Stein--Shakarchi, and the published set of R. C. Rhoades, *Solutions/Hints to the Exercises from Complex Analysis by Stein and Shakarchi* (2006), covers a selection of the chapter Exercises and not the Problems, so the derivation below is the card's throughout.

::: pf

::: {.pf-step #lem1}
For $\varepsilon>0$ and $t\in\RR$ put $P_\varepsilon(t)\coloneqq\frac{1}{\pi}\frac{\varepsilon}{t^2+\varepsilon^2}$. Then $\int_\RR P_\varepsilon(t)\,dt=1$, and for every $\gamma>0$

$$
\int_{\abs{t}>\gamma}P_\varepsilon(t)\,dt=\frac{2}{\pi}\arctan\frac{\varepsilon}{\gamma}\longrightarrow0\qquad(\varepsilon\to0^+).
$$

::: pf-proof
The substitution $t=\varepsilon u$ gives $\int_\RR P_\varepsilon=\frac1\pi\int_\RR\frac{du}{1+u^2}=1$ and $\int_{\abs{t}>\gamma}P_\varepsilon=\frac1\pi\int_{\abs{u}>\gamma/\varepsilon}\frac{du}{1+u^2}=1-\frac{2}{\pi}\arctan\frac{\gamma}{\varepsilon}=\frac{2}{\pi}\arctan\frac{\varepsilon}{\gamma}$, using $\arctan(1/s)=\frac\pi2-\arctan s$ for $s>0$. $\square$
:::

:::


::: {.pf-step #lem2}
Let $H\colon\RR\to\CC$ be continuous, bounded by $B$, and uniformly continuous; for instance $H$ the extension of $h$ by $0$ outside $[-M,M]$, which is uniformly continuous as soon as $h$ satisfies the Hölder condition of part (b) and $h(\pm M)=0$. Then

$$
\sup_{x\in\RR}\abs{\int_\RR P_\varepsilon(y-x)H(y)\,dy-H(x)}\longrightarrow0\qquad(\varepsilon\to0^+).
$$

::: pf-proof
Fix $\eta>0$ and choose $\gamma>0$ with $\abs{H(y)-H(x)}<\eta$ whenever $\abs{y-x}<\gamma$, uniformly in $x$ by uniform continuity. Then, since $\int_\RR P_\varepsilon=1$,

$$
\abs{\int_\RR P_\varepsilon(y-x)H(y)dy-H(x)}
\le\int_{\abs{y-x}<\gamma}P_\varepsilon(y-x)\eta\,dy+2B\int_{\abs{y-x}\ge\gamma}P_\varepsilon(y-x)\,dy
\le\eta+2B\cdot\frac{2}{\pi}\arctan\frac{\varepsilon}{\gamma},
$$

by Lemma 1, and the right side is $<\eta+2B\cdot\frac{2}{\pi}\frac{\varepsilon}{\gamma}$ for all $x$ at once. $\square$
:::

:::


::: {.pf-step #s4}
$g$ is holomorphic on $\Omega=\CC\setminus[-M,M]$.

::: pf-proof
The substitution $y=-M+2Ms$ turns the integral into an integral over $[0,1]$:

$$
g(z)=\frac{M}{\pi i}\int_0^1\frac{h(-M+2Ms)}{-M+2Ms-z}\,ds=\frac{M}{\pi i}\int_0^1F(z,s)\,ds,
\qquad F(z,s)\coloneqq\frac{h(-M+2Ms)}{-M+2Ms-z}.
$$

For each $s\in[0,1]$ the denominator $-M+2Ms-z$ is a non-zero holomorphic function of $z$ on $\Omega$ (its zero $-M+2Ms$ lies on $[-M,M]$), so $F(\cdot,s)$ is holomorphic on $\Omega$; and $F$ is continuous on $\Omega\times[0,1]$, because $h$ is continuous on $[-M,M]$ and $\abs{-M+2Ms-z}$ is continuous and nowhere zero there. By Theorem 5.4 of Chapter 2 [@SS03] the integral is holomorphic on $\Omega$.
:::

:::


::: {.pf-step #s5}
$g$ vanishes at infinity.

::: pf-proof
If $\abs{z}\ge2M$ and $\abs{y}\le M$ then $\abs{y-z}\ge\abs{z}-M\ge\abs{z}/2$, hence

$$
\abs{g(z)}\le\frac{1}{2\pi}\int_{-M}^{M}\frac{\abs{h(y)}}{\abs{y-z}}\,dy\le\frac{1}{2\pi}\cdot 2M\cdot\frac{B}{\abs{z}/2}=\frac{2MB}{\pi\abs{z}},
$$

so $\abs{g(z)}\to0$ as $\abs{z}\to\infty$; in particular $g$ is bounded on $\Omega\cap\{\abs z\ge2M\}$, where $\abs{g(z)}\le B/\pi$. Boundedness on the whole of $\Omega$ is not claimed and is false in general: step [](#s11){.pf-ref} shows that $g(M+i\varepsilon)$ grows like $\frac{\abs{h(M)}}{2\pi}\log\frac1\varepsilon$ when $h(M)\ne0$.
:::

:::


::: {.pf-step #s6}
$g(x+i\varepsilon)-g(x-i\varepsilon)=\int_{-M}^{M}P_\varepsilon(y-x)h(y)\dy$, and the jump of $g$ across the open interval is $h$, uniformly on compact subsets of $(-M,M)$.

::: pf-proof
For $x\in\RR$, $\varepsilon>0$ and $y\ne x$,

$$
\frac{1}{y-x-i\varepsilon}-\frac{1}{y-x+i\varepsilon}
=\frac{(y-x+i\varepsilon)-(y-x-i\varepsilon)}{(y-x)^2+\varepsilon^2}
=\frac{2i\varepsilon}{(y-x)^2+\varepsilon^2},
$$

so, by the definition of $g$ and the definition of $P_\varepsilon$,

$$
g(x+i\varepsilon)-g(x-i\varepsilon)
=\frac{1}{2\pi i}\int_{-M}^{M}h(y)\,\frac{2i\varepsilon}{(y-x)^2+\varepsilon^2}\,dy
=\int_{-M}^{M}P_\varepsilon(y-x)h(y)\,dy .
$$

Fix $0<\delta<M$ and $x\in[-M+\delta,M-\delta]$. Since $[-M,M]\supseteq[x-\delta,x+\delta]$,

$$
0\le 1-\int_{-M}^{M}P_\varepsilon(y-x)\,dy\le\int_{\abs{t}>\delta}P_\varepsilon(t)\,dt=\frac{2}{\pi}\arctan\frac{\varepsilon}{\delta}\longrightarrow0 ,
$$

and with $\gamma>0$ chosen so that $\abs{h(y)-h(x)}<\eta$ for $\abs{y-x}<\gamma$ (possible uniformly in $x$ because $h$ is uniformly continuous on the compact interval $[-M,M]$),

$$
\abs{\int_{-M}^{M}P_\varepsilon(y-x)h(y)dy-h(x)}
\le\eta+2B\int_{\abs{t}>\gamma}P_\varepsilon(t)\,dt+B\int_{\abs{t}>\delta}P_\varepsilon(t)\,dt .
$$

Hence the convergence holds uniformly on $[-M+\delta,M-\delta]$. This proves

$$
h(x)=\lim_{\substack{\varepsilon\to0\\ \varepsilon>0}}\bigl(g(x+i\varepsilon)-g(x-i\varepsilon)\bigr)
\qquad\text{for every }x\in(-M,M),
$$

uniformly on compact subsets of $(-M,M)$.
:::

:::


::: {.pf-step #s7}
At $x=\pm M$ the limit of $g(x+i\varepsilon)-g(x-i\varepsilon)$ is $h(\pm M)/2$, not $h(\pm M)$.

::: pf-proof
The same computation locates the limit at $x=\pm M$: with $y=M-u$,

$$
g(M+i\varepsilon)-g(M-i\varepsilon)=\frac{1}{\pi}\int_{0}^{2M}\frac{\varepsilon}{u^2+\varepsilon^2}h(M-u)\,du
\longrightarrow h(M)\cdot\frac{1}{\pi}\int_0^\infty\frac{du}{1+u^2}=\frac{h(M)}{2},
$$

and likewise at $-M$. So the printed identity "the jump of $g$ across $[-M,M]$ is $h$" holds on the open interval only: at an endpoint the segment bounds $\Omega$ from one side, half of the kernel mass falls outside $[-M,M]$, and the limit of the difference is $h(\pm M)/2$. On the open interval, where the jump is two-sided, the identity is exactly as printed.
:::

:::


::: {.pf-step #s9}
Step 4 (Plemelj): with $A(x)=\operatorname{PV}\int_{-M}^{M}\frac{h(y)}{y-x}\dy$ and $g^{\pm}(x)=\pm\frac{h(x)}{2}+\frac{1}{2\pi i}A(x)$, one has $g(x\pm i\varepsilon)\to g^{\pm}(x)$ uniformly on compact subsets of $(-M,M)$, so $g^{+}-g^{-}=h$ there.

::: pf-proof
For $x\in(-M,M)$ set

$$
A(x)\coloneqq\operatorname{PV}\!\int_{-M}^{M}\frac{h(y)}{y-x}\,dy,\qquad
g^{\pm}(x)\coloneqq\pm\frac{h(x)}{2}+\frac{1}{2\pi i}A(x).
$$

Then $A(x)$ is a well-defined finite number and

$$
g(x+i\varepsilon)\longrightarrow g^{+}(x),\qquad g(x-i\varepsilon)\longrightarrow g^{-}(x)
\qquad(\varepsilon\to0^+),
$$

uniformly on $[-M+\delta,M-\delta]$ for every $0<\delta<M$. In particular $g^{+}-g^{-}=h$ on $(-M,M)$.

*Proof.* Write $K_\varepsilon(u)\coloneqq u/(u^2+\varepsilon^2)$. For $x\in(-M,M)$, $\varepsilon>0$,

$$
\frac{1}{(y-x)-i\varepsilon}=\frac{(y-x)+i\varepsilon}{(y-x)^2+\varepsilon^2},
$$

so with $A_\varepsilon(x)\coloneqq\int_{-M}^{M}h(y)K_\varepsilon(y-x)\,dy$ and $B_\varepsilon(x)\coloneqq\varepsilon\int_{-M}^{M}\frac{h(y)}{(y-x)^2+\varepsilon^2}\,dy$,

$$
g(x+i\varepsilon)=\frac{1}{2\pi i}\bigl(A_\varepsilon(x)+iB_\varepsilon(x)\bigr),
\qquad
B_\varepsilon(x)=\pi\int_{-M}^{M}P_\varepsilon(y-x)h(y)\,dy .
$$

*(i) $A$ exists.* Since $\abs{\frac{h(y)-h(x)}{y-x}}\le C\abs{y-x}^{\alpha-1}$ is integrable on $[-M,M]$, and since $\operatorname{PV}\int_{-M}^M\frac{dy}{y-x}=\log\frac{M-x}{M+x}$ for $\abs{x}<M$ (the primitive is $\log\abs{y-x}$; the two sides give $\log(M-x)-\log(M+x)$),

$$
A(x)=\int_{-M}^{M}\frac{h(y)-h(x)}{y-x}\,dy+h(x)\log\frac{M-x}{M+x},
$$

so $A(x)$ is finite, and $A$ is continuous on $(-M,M)$ by dominated convergence.

*(ii) $B_\varepsilon\to\pi h$.* This is the estimate of Step 3: for $x\in[-M+\delta,M-\delta]$,

$$
\abs{\frac{B_\varepsilon(x)}{\pi}-h(x)}\le\eta(\gamma)+2B\int_{\abs{t}>\gamma}P_\varepsilon(t)\,dt+B\int_{\abs{t}>\delta}P_\varepsilon(t)\,dt
$$

with $\eta(\gamma)\coloneqq\sup\{\abs{h(y)-h(x)}:\abs{y-x}<\gamma\}$, which tends to $0$ with $\gamma$ uniformly in $x$ by uniform continuity of $h$ on $[-M,M]$.

*(iii) $A_\varepsilon\to A$.* Put $J_\varepsilon(x)\coloneqq\int_{-M}^{M}K_\varepsilon(y-x)\,dy=\frac12\log\frac{(M-x)^2+\varepsilon^2}{(M+x)^2+\varepsilon^2}$ and $J(x)\coloneqq\log\frac{M-x}{M+x}\ (=J_\varepsilon(x)$ with $\varepsilon=0)$. Subtracting the two expressions,

$$
A_\varepsilon(x)-A(x)=\int_{-M}^{M}\bigl(h(y)-h(x)\bigr)\Bigl(K_\varepsilon(y-x)-\frac{1}{y-x}\Bigr)dy+h(x)\bigl(J_\varepsilon(x)-J(x)\bigr).
$$

For $u\neq0$, $\abs{K_\varepsilon(u)-\frac1u}=\frac{\varepsilon^2}{\abs{u}(u^2+\varepsilon^2)}\le\min\Bigl(\frac{2}{\abs{u}},\frac{\varepsilon^2}{\abs{u}^3}\Bigr)$; and for $\abs{x}\le M-\delta$, $\abs{J_\varepsilon(x)-J(x)}\le\frac12\Bigl(\frac{\varepsilon^2}{(M-x)^2}+\frac{\varepsilon^2}{(M+x)^2}\Bigr)\le\frac{\varepsilon^2}{\delta^2}$, using $\abs{\log(1+s)}\le s$ for $s\ge0$. Hence, for any $\gamma>0$ and $\abs{x}\le M-\delta$,

$$
\abs{A_\varepsilon(x)-A(x)}
\le C\!\int_{\abs{u}\le\gamma}\!2\abs{u}^{\alpha-1}du+2B\!\int_{\abs{u}>\gamma}\!\frac{\varepsilon^2}{\abs{u}^3}du+\frac{B\varepsilon^2}{\delta^2}
=\frac{4C\gamma^{\alpha}}{\alpha}+\frac{2B\varepsilon^2}{\gamma^2}+\frac{B\varepsilon^2}{\delta^2},
$$

independently of $x$. Letting first $\varepsilon\to0^+$ and then $\gamma\to0^+$ proves (iii). Combining (i)–(iii) gives the claim, since $g(x+i\varepsilon)-g^{+}(x)=\frac{1}{2\pi i}\bigl(A_\varepsilon(x)-A(x)\bigr)+\frac{1}{2\pi}\bigl(B_\varepsilon(x)-\pi h(x)\bigr)$; the computation for $g(x-i\varepsilon)$ and $g^{-}(x)$ is the same with $\varepsilon$ replaced by $-\varepsilon$. $\square$

So without any hypothesis at the endpoints $g$ has the two boundary functions $g^{\pm}$, and $g^{+}-g^{-}=h$, on the open interval, uniformly on compact subsets.
:::

:::


::: {.pf-step #s10}
Step 5: if in addition $h(\pm M)=0$, the convergence is uniform on the closed interval $[-M,M]$.

::: pf-proof
Assume in addition $h(\pm M)=0$. Then the extension $H$ of $h$ by $0$ outside $[-M,M]$ satisfies the same Hölder inequality on all of $\RR$: for $y\in[-M,M]$ and $x>M$ one has $\abs{H(y)-H(x)}=\abs{h(y)}=\abs{h(y)-h(M)}\le C(y-M)^{\alpha}\le C\abs{y-x}^{\alpha}$, and symmetrically at $-M$. Consequently

$$
\sup_{x\in[-M,M]}\abs{g(x+i\varepsilon)-g^{+}(x)}\longrightarrow0,
\qquad
\sup_{x\in[-M,M]}\abs{g(x-i\varepsilon)-g^{-}(x)}\longrightarrow0
\qquad(\varepsilon\to0^+),
$$

where now $g^{\pm}(x)\coloneqq\pm\frac{h(x)}{2}+\frac{1}{2\pi i}A(x)$ and $A(x)\coloneqq\operatorname{PV}\int_\RR\frac{H(y)}{y-x}\,dy=\int_\RR\frac{H(y)-H(x)}{y-x}\,dy$; this $A$ agrees with the $A$ of Step 4 on $(-M,M)$, is continuous on $[-M,M]$, and $g^{\pm}(\pm M)$ are finite with $g^{+}(\pm M)=g^{-}(\pm M)=A(\pm M)/(2\pi i)$.

*Proof.* Because $\operatorname{PV}\int_\RR\frac{du}{u}=0$ (the symmetric limit of an odd integrand),

$$
A_\varepsilon(x)-A(x)=\int_\RR\bigl(H(y)-H(x)\bigr)\Bigl(K_\varepsilon(y-x)-\frac{1}{y-x}\Bigr)dy,
$$

the integrand now being integrable over all of $\RR$, and the estimate (iii) of Step 4, with $B$ the bound of $H$, applies verbatim and independently of $x$:

$$
\sup_{x\in\RR}\abs{A_\varepsilon(x)-A(x)}\le\frac{4C\gamma^{\alpha}}{\alpha}+\frac{2B\varepsilon^2}{\gamma^2}.
$$

Likewise $B_\varepsilon(x)=\pi\int_\RR P_\varepsilon(y-x)H(y)\,dy$ and Lemma 2 gives $\sup_{x\in\RR}\abs{B_\varepsilon(x)-\pi H(x)}\to0$. Both statements are uniform on $\RR$, hence on $[-M,M]$. $\square$
:::

:::


::: {.pf-step #s11}
Step 6 (the characterisation): $\mathcal C$ has at most one element, and $g\in\mathcal C$ if and only if $h(\pm M)=0$.

::: pf-proof
Let $\mathcal{C}$ be the class of functions $G$ with

- (i) $G$ holomorphic on $\Omega$;
- (ii) $G(z)\to0$ as $\abs{z}\to\infty$;
- (iii) $G(x+i\varepsilon)$ and $G(x-i\varepsilon)$ converge as $\varepsilon\to0^+$, uniformly in $x\in[-M,M]$, to functions $G^{+},G^{-}$ continuous on $[-M,M]$ with $G^{+}-G^{-}=h$.

Then:

1. $\mathcal{C}$ has at most one element;
2. $g\in\mathcal{C}$ if and only if $h(\pm M)=0$. In particular, if $h$ vanishes at $\pm M$ — for instance if the support of $h$ is a compact subset of $(-M,M)$ — then $g$ is the unique holomorphic function satisfying (i), (ii), (iii), as the problem asserts.

*Proof of 1.* Let $G_1,G_2\in\mathcal{C}$ and put $H\coloneqq G_1-G_2$. Then $H$ is holomorphic on $\Omega$, $H(z)\to0$ as $\abs{z}\to\infty$, and $H(x\pm i\varepsilon)$ converge uniformly on $[-M,M]$ to $H^{\pm}\coloneqq G_1^{\pm}-G_2^{\pm}$, with $H^{+}-H^{-}=h-h=0$.

*(a) $H$ is holomorphic on $\CC\setminus\{M,-M\}$.* $H$ is holomorphic on the upper half-plane and on the lower half-plane, both of which lie in $\Omega$. It extends continuously to $I\coloneqq\RR\setminus\{\pm M\}$ from either side, and the two extensions agree on $I$: on $(-M,M)$ because $H^{+}-H^{-}=0$ there, and on $\{\abs{x}>M\}$ because $H$ is holomorphic, hence continuous, in a neighbourhood of such an $x$. The region $\CC\setminus\{M,-M\}$ has $I$ as its part on $\RR$; by Theorem 5.5 of Chapter 2 (the symmetry principle) [@SS03] the function glued from $H$ above and below $I$ is holomorphic on $\CC\setminus\{M,-M\}$.

*(b) $H$ is bounded near $\pm M$.* Fix $0<r<M$ and let $U\coloneqq\{z:\abs{z-M}<r,\ \operatorname{Im}z>0\}$. Then $H$ is holomorphic on $U$ and continuous on $\overline{U}$: on the diameter $(M-r,M+r)$ the limit from above is $H^{+}$, continuous on $[-M,M]$ and in particular at $x=M$, and on $(M,M+r)$ it is $H$ itself. So Corollary 4.6 of Chapter 3 (the maximum modulus principle on a region with compact closure) [@SS03] gives

$$
\sup_{z\in U}\abs{H(z)}\le\sup_{z\in\overline U\setminus U}\abs{H(z)}<\infty .
$$

The same argument with $\operatorname{Im}z<0$ bounds $H$ on $\{0<\abs{z-M}<r\}$, and $M$ may be replaced by $-M$.

*(c) $H$ is entire.* By Theorem 3.1 of Chapter 3 (Riemann's theorem on removable singularities) [@SS03] the bounded holomorphic function $H$ on the punctured discs at $M$ and at $-M$ extends holomorphically across both points.

*(d) $H\equiv0$.* $H$ is entire and $H(z)\to0$ as $\abs{z}\to\infty$, so $H$ is bounded; by Corollary 4.5 of Chapter 2 (Liouville's theorem) [@SS03] $H$ is constant, and its limit at infinity is $0$. Hence $G_1=G_2$. $\square$

*Proof of 2.* If $h(\pm M)=0$, Step 5 exhibits the limits, so $g\in\mathcal{C}$. Conversely let $h(M)\ne0$. Substituting $y=M-u$, $u\in[0,2M]$, and using $\abs{u+i\varepsilon}\ge\max(u,\varepsilon)$,

$$
g(M+i\varepsilon)=-\frac{1}{2\pi i}\int_0^{2M}\frac{h(M-u)}{u+i\varepsilon}\,du .
$$

Write $h(M-u)=h(M)+\rho(u)$ with $\abs{\rho(u)}\le Cu^{\alpha}$. Then $\abs{\int_0^{2M}\frac{\rho(u)}{u+i\varepsilon}du}\le C\int_0^{2M}u^{\alpha-1}du=\frac{C(2M)^{\alpha}}{\alpha}$, while

$$
\int_0^{2M}\frac{du}{u+i\varepsilon}=\log(2M+i\varepsilon)-\log(i\varepsilon)=\log\frac{2M}{\varepsilon}-\frac{\pi i}{2}+o(1)\qquad(\varepsilon\to0^+).
$$

Hence

$$
\abs{g(M+i\varepsilon)}=\frac{\abs{h(M)}}{2\pi}\log\frac1\varepsilon+O(1)\longrightarrow\infty ,
$$

and the same holds at $-M$ and for $g(M-i\varepsilon)$. So $g(M+i\varepsilon)$ has no finite limit as $\varepsilon\to0^+$, and (iii) fails. $\square$
:::

:::

:::

**Remarks on the printed statement.**

1. **The jump identity is an identity on the open interval.** On $(-M,M)$ it holds exactly as printed, and in fact uniformly on compact subsets (Steps 3 and 4). At $x=\pm M$ the limit of $g(x+i\varepsilon)-g(x-i\varepsilon)$ is $h(\pm M)/2$, because half of the mass of the kernel $P_\varepsilon$ falls outside $[-M,M]$; there the segment bounds $\Omega$ from one side only, so no two-sided jump exists.

2. **Condition (iii) is a statement about uniformity on the closed interval, and $g$ satisfies it precisely when $h(\pm M)=0$.** If $h(\pm M)\ne0$, Step 6 shows $g(M\pm i\varepsilon)$ grows like $\frac{\abs{h(M)}}{2\pi}\log\frac1\varepsilon$; the limits $g^{\pm}$ then exist only on the open interval (Step 4). Both versions are recorded above.

3. **The book's hint is exactly the endpoint hypothesis.** "If $G$ is another function satisfying these conditions, $g-G$ is entire" is the content of Step 6(a)–(c): the symmetry principle gives holomorphy away from $\pm M$, and it is the uniform convergence *on the closed interval* that makes $H$ continuous on the closed half-discs, whence bounded near $\pm M$ by the maximum modulus principle and removable by Riemann's theorem.

4. **That hypothesis cannot be dropped.** If (iii) is weakened to convergence uniformly on compact subsets of $(-M,M)$ — the conclusion of Step 4, which holds for every Hölder $h$ — the characterisation fails: then

$$
G(z)\coloneqq g(z)+\frac{1}{z^2-M^2}
$$

also satisfies (i) and (ii) (its only poles are at $\pm M\notin\Omega$), and $G(x\pm i\varepsilon)$ converge uniformly on compact subsets of $(-M,M)$ with $G^{+}-G^{-}=h$, since $\frac{1}{z^2-M^2}$ is continuous at every point of $(-M,M)$ and has the same limit from either side; yet $G\ne g$, and $G-g$ is not entire. So what singles $g$ out is the boundedness of $G-g$ near the two endpoints — the hypothesis that makes $G-g$ entire — and not condition (iii) alone.
:::
