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
---

::: {.exercise}

Verify the statements made in Example 4 of §38, which reads: for $X=(0,1)$, a bounded continuous function $f:X\to\RR$ is extendable to the one-point compactification of Example 1 if and only if the limits
$$
\lim_{x\to0^+}f(x)\qquad\text{and}\qquad\lim_{x\to1^-}f(x)
$$
exist and are equal; it is extendable to the two-point compactification of Example 2 if and only if both these limits simply exist; and for the compactification of Example 3, extensions exist for a broader class of functions, since $f$ is extendable if both limits exist, and the function $f(x)=\sin(1/x)$ is also extendable.
:::

::: {.solution}
Write $X=(0,1)$ and let $f:X\to\RR$ be bounded and continuous. For $x_0\in\{0,1\}$ we say that $\lim_{x\to x_0}f(x)$ exists if $f(x_n)$ converges for every sequence $x_n\to x_0$ in $X$ and the limit does not depend on the sequence; this sequential form is the ordinary one because $X$ is first countable.

(1) The one-point compactification (Example 1). Let $X^*=X\cup\{\infty\}$ and suppose that both limits exist and are equal to some $c$; define $F:X^*\to\RR$ by $F|X=f$ and $F(\infty)=c$. If $x_n\to\infty$ in $X^*$, then every compact subset of $X$ contains only finitely many of the $x_n$, and the compact subsets of $(0,1)$ are the closed bounded ones, so either $x_n\to0$ or $x_n\to1$ along a subsequence. Every subsequence of $(x_n)$ has a further subsequence converging to $0$ or to $1$, and along it $f\to c$; hence $f(x_n)\to c=F(\infty)$. As $X^*$ is first countable, this gives continuity of $F$ at $\infty$, and $F$ is continuous elsewhere because $f$ is. Conversely, if $F:X^*\to\RR$ extends $f$ continuously, then for any sequence $x_n\to0$ in $X$ one has $x_n\to\infty$ in $X^*$, so $f(x_n)=F(x_n)\to F(\infty)$ and $\lim_{x\to0^+}f=F(\infty)$; likewise $\lim_{x\to1^-}f=F(\infty)$. So the two limits exist and are equal.

(2) The two-point compactification $[0,1]$ (Example 2). If both limits exist, say $a$ at $0$ and $b$ at $1$, define $F$ on $[0,1]$ by $F(0)=a$, $F(1)=b$ and $F|X=f$; it is continuous at $0$ and at $1$ by the sequential criterion and on $X$ by continuity of $f$. Conversely, a continuous extension $F$ to $[0,1]$ gives $\lim_{x\to0^+}f=F(0)$ and $\lim_{x\to1^-}f=F(1)$, which therefore exist and may differ.

(3) The compactification of Example 3. Let $e(x)=(x,\sin(1/x))$ and $Y=\overline{e(X)}$ in $\RR^2$, so that
$$
Y=e(X)\cup(\{0\}\times[-1,1])\cup\{(1,\sin1)\}.
$$
Suppose both limits exist, $a=\lim_{x\to0^+}f$ and $b=\lim_{x\to1^-}f$, and define $F:Y\to\RR$ by $F(e(x))=f(x)$ for $x\in X$, $F(0,t)=a$ for $t\in[-1,1]$, and $F(1,\sin1)=b$. Let $y_n\to p$ in $Y$; we show $F(y_n)\to F(p)$. If $p=e(x)$ with $x\in X$, then $y_n\in e(X)$ for large $n$ and $F(y_n)=f(x_n)\to f(x)$ with $x_n\to x$. If $p=(0,t)$, then for each $n$ either $y_n=e(x_n)$, in which case $F(y_n)=f(x_n)$ and $x_n\to0$, or $y_n\in\{0\}\times[-1,1]$, where $F$ takes the value $a$; the two cases can be mixed, and replacing each term that lies in $\{0\}\times[-1,1]$ by $e(x'_n)$ with $x'_n\to0$ close enough to make $\abs{f(x'_n)-a}<1/n$ leaves $F(y_n)\to a=F(p)$. The case $p=(1,\sin1)$ is the same with $x_n\to1$ and $b$. Hence $F$ is sequentially continuous on the metric space $Y$, so continuous.

The function $\sin(1/x)=\pi_2\circ e$ is the restriction to $e(X)$ of $\pi_2|Y$, which is continuous, so it extends to $Y$ even though $\lim_{x\to0^+}\sin(1/x)$ does not exist; this is the case Example 4 mentions. The function $\cos(1/x)$ does not extend to $Y$: that is Exercise 38.2, whose card (E-UB4PP) proves it.
:::
