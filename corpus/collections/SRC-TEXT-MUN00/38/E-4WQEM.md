---
schema: qual/card@1
id: E-4WQEM
kind: problem
title: Verifying the statements of Example 4 on compactifications of $(0,1)$
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §37--§42 of SRC-TEXT-MUN00.
    Searched: "Solutions to exercises in Munkres", file S38.pdf, whose section 38 begins at Exercise 38.4;
    "Solutions to exercises for Mathematics 205A" (University of California, Riverside, Fall 2014), file
    solutions5a.pdf, whose section VI.4 answers §38 Exercises 2 and 3 only; Ana Emilia de Orellana,
    "Solutions --- Topology Munkres", whose contents stop at §34 and §37; "Doug's World", Chapter 4 only;
    Dan Whitman (to §22), "positron0802" (Chapters 2 and 3), "shenapse" (§1--§11), "9beach" (§1--§4),
    "kyp44" (§1--§22); and the dbFin pages, which have no chapter-5 or chapter-6 section. What was
    repaired: the card's stored statement read "Verify the statements made in Example 4 ... concerning
    the one-point compactification of X = (0,1) obtained from the imbedding h with component functions x
    and sin(1/x)", which is Example 3, and its proof then verified Example 3's compactification alone;
    the card now states the printed exercise and proves each statement Example 4 makes, one for each of
    the three compactifications. Checked against Munkres, Topology (2000), Example 4 of §38 (printed p.
    238) and Exercise 1 of §38 (printed p. 241), with Examples 1--3 of §38, Theorem 29.1 (the one-point
    compactification), Theorem 21.3 and its sequential criterion, and Theorem 23.3. Not checked here: the
    book's "still broader class" in Example 4 is illustrated, not classified; the card proves the two
    claims Example 4 makes about Example 3, and Exercise 38.2's failure of cos(1/x) is left to its own
    card.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    A review finding corrected the page of the source citation. The 2026-11-10 note above records
    "Example 4 of §38 (printed p. 238)", and that page is wrong: in the Egbert copy of Munkres, Topology
    (2000), printed p. 238 is PDF p. 253 and carries Examples 1 and 2 of §38, while Example 4 -- "Let
    X = (0,1). Consider the one-point compactification of X given in Example 1 ..." -- begins on printed
    p. 239, PDF p. 254, which was read here on that page. Example 4 of §38 is therefore printed p. 239.
    Nothing else changes: the exercise answered is Exercise 1 of §38 (printed p. 241), and the proof's
    own citations -- Examples 1 to 3 of §38, Theorem 29.1, Theorem 21.3, Theorem 23.3 -- are unaffected.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read for #169 against §38 Exercise 1 and the three statements of Example 4 of §38, and found
    correct. Searched first for a published proof: Poulsen's §38 sheet covers Exercises 38.4 to
    38.9 and stops there, dbFin's index stops at §67 with a gap before it, and no other retained
    set reaches §38; so nothing is transcribed and the verification is the card's own. (1) The
    one-point compactification: the card proves both directions, and the only-if direction turns on
    the neighbourhoods of the point at infinity, a sequence converging to $0$ in $(0,1)$ leaving
    every compact subset of $(0,1)$, each of which is closed and bounded in $\RR$ by Theorem 27.3
    and hence bounded away from $0$. (2) The two-point compactification $[0,1]$: the same argument
    with the two ends separated, the limits need not agree. (3) The compactification $Y$ of
    Example 3, the closure of $e(X)$ for $e(x)=(x,\sin(1/x))$: a function whose two limits exist
    extends by the values $a$ and $b$ prescribed on $\{0\}\times[-1,1]$ and at $(1,\sin 1)$, which
    is continuous because $f(x)$ tends to those values as $x$ tends to the ends; and
    $\sin(1/x)=\pi_2\circ e$ extends as the restriction of the second projection, although it has
    no limit at $0^{+}$. That is Example 4's claim that the class of functions extending grows
    from (1) to (2) to (3), and the card also records the step from (3) to the construction of
    Theorem 38.2, where the coordinates of an imbedding are exactly the bounded continuous
    functions that extend. Not checked: no published solution was located, and none is claimed.
---

::: {.exercise}

Verify the statements made in Example 4 of §38, which reads: for $X=(0,1)$, a bounded continuous function $f:X\to\RR$ is extendable to the one-point compactification of Example 1 if and only if the limits
$$
\lim_{x\to0^+}f(x)\qquad\text{and}\qquad\lim_{x\to1^-}f(x)
$$
exist and are equal; it is extendable to the two-point compactification of Example 2 if and only if both these limits simply exist; and for the compactification of Example 3, extensions exist for a broader class of functions, since $f$ is extendable if both limits exist, and the function $f(x)=\sin(1/x)$ is also extendable.
:::

::: {.solution}

The verification is the card's own; no published solution of Munkres §38 Exercise 1 was located, and the sets searched are recorded in the audit trail.

Write $X=(0,1)$ and let $f:X\to\RR$ be bounded and continuous. Since $X$ is first countable, $\lim_{x\to0^{+}}f$ exists with value $c$ exactly when $f(x_{n})\to c$ for every sequence $x_{n}\to0$ in $X$, and likewise at $1$ (§21).

::: pf

::: {.pf-step #one-point}
(1) For the one-point compactification $X^{*}=X\cup\{\infty\}$ of Example 1, $f$ extends continuously to $X^{*}$ exactly when both limits exist and are equal.

::: pf-proof

::: {.pf-step #one-point-if}
If both limits exist and equal $c$, then $f$ extends continuously with $F(\infty)=c$.

::: pf-proof
Define $F:X^{*}\to\RR$ by $\restrictionof{F}{X}=f$ and $F(\infty)=c$; it is continuous on the open subspace $X$. For continuity at $\infty$ let $\varepsilon>0$ and choose $\delta_{0},\delta_{1}>0$ with $\abs{f(x)-c}<\varepsilon$ for $0<x<\delta_{0}$ and for $1-\delta_{1}<x<1$. The set $K=X\cap[\delta_{0},1-\delta_{1}]$ is closed and bounded in $\RR$, hence compact, so $X^{*}\setminus K$ is a neighbourhood of $\infty$ (§29). Every $x\in X^{*}\setminus K$ lies in $X$ with $x<\delta_{0}$ or $x>1-\delta_{1}$, or else equals $\infty$; in each case $\abs{F(x)-c}<\varepsilon$, since $F(\infty)=c$. So $F$ is continuous at $\infty$.
:::

:::

::: {.pf-step #one-point-only-if}
If $F:X^{*}\to\RR$ extends $f$ continuously, then both limits exist and equal $F(\infty)$.

::: pf-proof
Let $x_{n}\to0$ in $X$. Every compact subset of $X$ is closed and bounded in $\RR$ (Theorem 27.3), so it omits all but finitely many of the $x_{n}$, and therefore $x_{n}\to\infty$ in $X^{*}$: the neighbourhoods of $\infty$ are the complements of compact sets. Continuity of $F$ gives $f(x_{n})=F(x_{n})\to F(\infty)$, so $\lim_{x\to0^{+}}f=F(\infty)$; the same argument with $x_{n}\to1$ gives $\lim_{x\to1^{-}}f=F(\infty)$.
:::

:::

::: {.pf-qed}
Steps [](#one-point-if){.pf-ref} and [](#one-point-only-if){.pf-ref} are the two directions of (1), in which the limits must be equal because both equal $F(\infty)$.
:::

:::

:::

::: {.pf-step #two-point}
(2) For the two-point compactification $[0,1]$ of Example 2, $f$ extends continuously exactly when both limits exist.

::: pf-proof
If $\lim_{x\to0^{+}}f=a$ and $\lim_{x\to1^{-}}f=b$ exist, define $F:[0,1]\to\RR$ by $F(0)=a$, $F(1)=b$ and $\restrictionof{F}{X}=f$; continuity at $0$ and at $1$ is the sequential criterion just used, and on $X$ it is the continuity of $f$. Conversely a continuous $F:[0,1]\to\RR$ extending $f$ gives $f(x_{n})=F(x_{n})\to F(0)$ for $x_{n}\to0$ and $f(x_{n})\to F(1)$ for $x_{n}\to1$, so both limits exist, with values $F(0)$ and $F(1)$, which need not be equal.
:::

:::

::: {.pf-step #example-3}
(3) For the compactification $Y=\overline{e(X)}$ of Example 3, with $e(x)=\big(x,\sin(1/x)\big)$, every $f$ whose two limits exist extends, and so does $\sin(1/x)$.

::: pf-proof

::: {.pf-step #y-structure}
$Y=e(X)\cup\big(\{0\}\times[-1,1]\big)\cup\{(1,\sin1)\}$.

::: pf-proof
$e$ is continuous on $X$, and as $x\to0^{+}$ the first coordinate tends to $0$ while $\sin(1/x)$ ranges over $[-1,1]$, all of whose points are limits of values of $\sin(1/x)$; so $\{0\}\times[-1,1]\subset\overline{e(X)}$. As $x\to1^{-}$, $e(x)\to(1,\sin1)$. Conversely a sequence in $e(X)$ converging in $\RR^{2}$ has first coordinates converging to some $t\in[0,1]$, and if $t\in(0,1)$ the limit is $e(t)$, while $t=0$ gives a point of $\{0\}\times[-1,1]$ and $t=1$ gives $(1,\sin1)$. So $Y$ is that union (Example 3 of §38).
:::

:::

::: {.pf-step #extension}
If $\lim_{x\to0^{+}}f=a$ and $\lim_{x\to1^{-}}f=b$ exist, then $f\circ e^{-1}$ extends continuously to $Y$.

::: pf-proof
Define $F:Y\to\RR$ by $F\big(e(x)\big)=f(x)$ for $x\in X$, $F(0,t)=a$ for $t\in[-1,1]$, and $F(1,\sin1)=b$; this is well defined by step [](#y-structure){.pf-ref}. Let $y_{n}\to p$ in $Y$. If $p=e(x)$ with $x\in X$, then for large $n$ the first coordinate of $y_{n}$ lies in $X$, so $y_{n}=e(x_{n})$ with $x_{n}\to x$, and $F(y_{n})=f(x_{n})\to f(x)=F(p)$. If $p=(0,t)$, write $c_{n}$ for the first coordinate of $y_{n}$, which tends to $0$; then $F(y_{n})=f(c_{n})$ when $c_{n}>0$ and $F(y_{n})=a$ when $c_{n}=0$, and in both cases $\abs{F(y_{n})-a}<\varepsilon$ for all large $n$ once $\varepsilon>0$ is given and $\delta$ is chosen with $\abs{f(x)-a}<\varepsilon$ for $0<x<\delta$. So $F(y_{n})\to a=F(p)$. The case $p=(1,\sin1)$ is the same with $c_{n}\to1$ and $b$ in place of $a$. Hence $F$ is continuous, $Y$ being metric.
:::

:::

::: {.pf-step #sin}
$\sin(1/x)$ extends to $Y$ although $\lim_{x\to0^{+}}\sin(1/x)$ does not exist.

::: pf-proof
$\sin(1/x)=\pi_{2}\big(e(x)\big)$ is the restriction to $e(X)$ of the continuous function $\restrictionof{\pi_{2}}{Y}$, which extends it. The limit at $0^{+}$ does not exist, since $\sin(1/x)=1$ at $x=1/(\pi/2+2\pi k)$ and $-1$ at $x=1/(3\pi/2+2\pi k)$ for every $k$, two sequences tending to $0$. So Example 3 extends a strictly larger class of functions than Example 2, as Example 4 states.
:::

:::

::: {.pf-qed}
Step [](#extension){.pf-ref} gives the extension whenever the two limits exist, as in (2) and unlike (1); step [](#sin){.pf-ref} extends a function for which no limit at $0^{+}$ exists, so the class of extendable functions for this compactification is strictly larger than the class of (2).
:::

:::

:::

:::
:::
