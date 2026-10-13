---
schema: qual/card@1
id: P-SERIES-A2-08
kind: problem
title: Convergence of $\sum p^nn^p$, $\sum\frac{n!}{n^n}$, $\sum(n^{1/n}-1)^n$ and related series
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Investigate each series for convergence, divergence, conditional convergence, and absolute convergence. Where parameters occur, determine the parameter ranges for each behavior.

1. $\displaystyle\sum_{n=1}^\infty p^n n^p$, with $p>0$.
2. $\displaystyle\sum_{n=1}^\infty (-1)^n\frac{\sqrt{n+1}-\sqrt n}{n^p}$.
3. $\displaystyle\sum_{n=1}^\infty\frac1{p^n-q^n}$, with $0<q<p$.
4. $\displaystyle\sum_{n=1}^\infty\frac{n!}{n^n}$.
5. $\displaystyle\sum_{n=1}^\infty\left(n^{1/n}-1\right)^n$.
6. $\displaystyle\sum_{n=1}^\infty\frac1{1+r^n}$.
:::

::: {.solution}
## Series 1

Consider
\[
\sum_{n=1}^{\infty}p^n n^p,
\qquad
p>0.
\]
Let
\[
a_n=p^n n^p.
\]

<1>1. The \(n\)th root is
\[
\boxed{
a_n^{1/n}
=
p\,n^{p/n}}.
\]

::: {.proof}
\[
(p^nn^p)^{1/n}
=
p\,n^{p/n}.
\]
:::

<1>2. One has
\[
\boxed{
n^{p/n}\to1}.
\]

::: {.proof}
\[
n^{p/n}
=
\exp\left(
p\frac{\log n}{n}
\right),
\]
and
\[
\frac{\log n}{n}\to0.
\]
:::

<1>3. Therefore
\[
\boxed{
\lim_{n\to\infty}a_n^{1/n}=p}.
\]

::: {.proof}
Combine steps <1>1--<1>2.
:::

<1>4. If
\[
0<p<1,
\]
the series converges absolutely.

::: {.proof}
The root-test limit in step <1>3 is \(<1\). The terms are nonnegative, so
convergence is automatically absolute.
:::

<1>5. If
\[
p>1,
\]
the series diverges.

::: {.proof}
The root-test limit is \(>1\).
:::

<1>6. If
\[
p=1,
\]
the terms are
\[
a_n=n,
\]
so the series diverges.

::: {.proof}
The terms do not tend to zero.
:::

<1>7. Thus Series 1 converges exactly for
\[
\boxed{0<p<1}
\]
and diverges for
\[
\boxed{p\ge1}.
\]

::: {.proof}
Combine steps <1>4--<1>6.
:::

## Series 2

Consider
\[
\sum_{n=1}^{\infty}
(-1)^n
\frac{\sqrt{n+1}-\sqrt n}{n^p}.
\]
Let
\[
b_n
=
\frac{\sqrt{n+1}-\sqrt n}{n^p}.
\]

<1>8. Rationalizing,
\[
\boxed{
b_n
=
\frac1{
n^p(\sqrt{n+1}+\sqrt n)}}.
\]

::: {.proof}
\[
\sqrt{n+1}-\sqrt n
=
\frac1{\sqrt{n+1}+\sqrt n}.
\]
:::

<1>9. Factoring \(\sqrt n\),
\[
\boxed{
b_n
=
\frac{
n^{-(p+1/2)}
}{
\sqrt{1+1/n}+1}}.
\]

::: {.proof}
\[
\sqrt{n+1}+\sqrt n
=
\sqrt n
\left(
\sqrt{1+1/n}+1
\right).
\]
:::

<1>10. Hence
\[
\boxed{
\frac{
b_n
}{
n^{-(p+1/2)}
}
\longrightarrow
\frac12}.
\]

::: {.proof}
The denominator
\[
\sqrt{1+1/n}+1
\]
tends to \(2\).
:::

<1>11. Therefore
\[
\sum b_n
\]
converges exactly when
\[
\boxed{p>\frac12}.
\]

::: {.proof}
By step <1>10, \(\sum b_n\) is limit-comparable to the \(p\)-series
\[
\sum n^{-(p+1/2)}.
\]
This converges exactly when
\[
p+\frac12>1.
\]
:::

<1>12. The terms \(b_n\) tend to zero exactly when
\[
\boxed{p>-\frac12}.
\]

::: {.proof}
From step <1>9:
- if \(p+\tfrac12>0\), then \(n^{-(p+1/2)}\to0\);
- if \(p+\tfrac12=0\), then \(b_n\to1/2\);
- if \(p+\tfrac12<0\), then \(b_n\to+\infty\).
:::

<1>13. Assume
\[
p>-\frac12.
\]
Then \(b_n\) is eventually decreasing.

::: {.proof}
For real \(x>0\), set
\[
D(x)
=
x^p
\left(
\sqrt{x+1}+\sqrt x
\right),
\qquad
b(x)=\frac1{D(x)}.
\]
A logarithmic derivative gives
\[
\frac{D'(x)}{D(x)}
=
\frac px
+
\frac1{2\sqrt{x(x+1)}}.
\]
Multiplying by \(x\),
\[
x\frac{D'(x)}{D(x)}
=
p+\frac12\sqrt{\frac{x}{x+1}}
\longrightarrow
p+\frac12>0.
\]
Hence \(D'(x)>0\) for all sufficiently large \(x\), so \(D(n)\) is
eventually increasing and \(b_n=1/D(n)\) is eventually decreasing.
:::

<1>14. Therefore the alternating series
\[
\sum (-1)^n b_n
\]
converges whenever
\[
\boxed{p>-\frac12}.
\]

::: {.proof}
By step <1>12, \(b_n\to0\), and by step <1>13, \(b_n\) is eventually
decreasing. The alternating-series test applies after discarding finitely
many initial terms.
:::

<1>15. If
\[
p\le-\frac12,
\]
the alternating series diverges.

::: {.proof}
By step <1>12, \(b_n\not\to0\). Therefore the terms
\[
(-1)^n b_n
\]
do not tend to zero.
:::

<1>16. Hence Series 2 is
\[
\boxed{\text{absolutely convergent for }p>\frac12,}
\]
\[
\boxed{\text{conditionally convergent for }-\frac12<p\le\frac12,}
\]
and
\[
\boxed{\text{divergent for }p\le-\frac12.}
\]

::: {.proof}
Absolute convergence is step <1>11. Ordinary convergence is steps
<1>14--<1>15. The conditional range is the difference between the ordinary
and absolute convergence ranges.
:::

## Series 3

Consider
\[
\sum_{n=1}^{\infty}
\frac1{p^n-q^n},
\qquad
0<q<p.
\]

<1>17. Write
\[
\boxed{
\frac1{p^n-q^n}
=
\frac1{
p^n\left(1-(q/p)^n\right)}}.
\]

::: {.proof}
Factor \(p^n\) from the denominator.
:::

<1>18. Since
\[
0<\frac qp<1,
\]
one has
\[
\left(\frac qp\right)^n\to0.
\]

::: {.proof}
This is a geometric sequence with ratio in \((0,1)\).
:::

<1>19. Therefore
\[
\boxed{
\frac{
1/(p^n-q^n)
}{
1/p^n
}
=
\frac1{1-(q/p)^n}
\longrightarrow1}.
\]

::: {.proof}
Use step <1>18.
:::

<1>20. Hence Series 3 has the same convergence behavior as
\[
\sum\frac1{p^n}.
\]

::: {.proof}
Apply the limit-comparison test using step <1>19.
:::

<1>21. Thus Series 3 converges exactly when
\[
\boxed{p>1}
\]
and diverges when
\[
\boxed{0<p\le1}.
\]

::: {.proof}
The comparison series is geometric with ratio \(1/p\). It converges exactly
when
\[
1/p<1.
\]
:::

## Series 4

Consider
\[
\sum_{n=1}^{\infty}\frac{n!}{n^n}.
\]
Set
\[
a_n=\frac{n!}{n^n}.
\]

<1>22. The ratio is
\[
\boxed{
\frac{a_{n+1}}{a_n}
=
\left(
\frac{n}{n+1}
\right)^n}.
\]

::: {.proof}
\[
\begin{aligned}
\frac{a_{n+1}}{a_n}
&=
\frac{(n+1)!}{(n+1)^{n+1}}
\frac{n^n}{n!}\\
&=
\frac{(n+1)n^n}{(n+1)^{n+1}}\\
&=
\left(
\frac n{n+1}
\right)^n.
\end{aligned}
\]
:::

<1>23. One has
\[
\boxed{
\left(
\frac n{n+1}
\right)^n
=
\left(
1+\frac1n
\right)^{-n}
\longrightarrow e^{-1}}.
\]

::: {.proof}
Use the standard limit
\[
\left(
1+\frac1n
\right)^n\to e.
\]
:::

<1>24. Therefore Series 4
\[
\boxed{\text{converges absolutely}}.
\]

::: {.proof}
The ratio-test limit is
\[
e^{-1}<1.
\]
The terms are nonnegative.
:::

## Series 5

Consider
\[
\sum_{n=1}^{\infty}
\left(
n^{1/n}-1
\right)^n.
\]
Set
\[
a_n
=
\left(
n^{1/n}-1
\right)^n.
\]

<1>25. The \(n\)th root is
\[
\boxed{
a_n^{1/n}
=
n^{1/n}-1}.
\]

::: {.proof}
The terms are nonnegative.
:::

<1>26. One has
\[
\boxed{
n^{1/n}\to1}.
\]

::: {.proof}
\[
n^{1/n}
=
e^{(\log n)/n}
\to
e^0
=
1.
\]
:::

<1>27. Hence
\[
\boxed{
a_n^{1/n}\to0}.
\]

::: {.proof}
Subtract \(1\) from the limit in step <1>26.
:::

<1>28. Therefore Series 5
\[
\boxed{\text{converges absolutely}}.
\]

::: {.proof}
The root-test limit is
\[
0<1.
\]
:::

## Series 6

Consider
\[
\sum_{n=1}^{\infty}\frac1{1+r^n},
\]
for real \(r\) whenever the terms are defined.

<1>29. If
\[
|r|<1,
\]
then
\[
r^n\to0
\]
and therefore
\[
\boxed{
\frac1{1+r^n}\to1}.
\]

::: {.proof}
Use continuity of
\[
x\mapsto\frac1{1+x}
\]
at \(x=0\).
:::

<1>30. Hence the series diverges when
\[
\boxed{|r|<1}.
\]

::: {.proof}
The terms do not tend to zero.
:::

<1>31. If
\[
r=1,
\]
then every term equals \(1/2\), so the series diverges.

::: {.proof}
\[
\frac1{1+1^n}
=
\frac12.
\]
:::

<1>32. If
\[
r=-1,
\]
the series is not defined.

::: {.proof}
For odd \(n\),
\[
1+r^n
=
1-1
=
0.
\]
:::

<1>33. Assume
\[
|r|>1.
\]
Then
\[
\boxed{
\frac1{1+r^n}
=
\frac{r^{-n}}{1+r^{-n}}}.
\]

::: {.proof}
Divide numerator and denominator by \(r^n\).
:::

<1>34. Since
\[
r^{-n}\to0,
\]
there exists \(N\) such that for \(n\ge N\),
\[
|1+r^{-n}|\ge\frac12.
\]

::: {.proof}
Choose \(N\) so that
\[
|r^{-n}|<\frac12.
\]
Then the reverse triangle inequality gives
\[
|1+r^{-n}|
\ge
1-|r^{-n}|
>
\frac12.
\]
:::

<1>35. For \(n\ge N\),
\[
\left|
\frac1{1+r^n}
\right|
\le
2|r|^{-n}.
\]

::: {.proof}
Use step <1>33 and the denominator bound in step <1>34.
:::

<1>36. Therefore Series 6 converges absolutely for
\[
\boxed{|r|>1}.
\]

::: {.proof}
The geometric series
\[
\sum |r|^{-n}
\]
converges because
\[
|r|^{-1}<1.
\]
Apply the comparison test using step <1>35.
:::

<1>37. Thus, for real \(r\), Series 6 is
\[
\boxed{\text{absolutely convergent for }|r|>1,}
\]
\[
\boxed{\text{divergent for }|r|<1\text{ or }r=1,}
\]
while
\[
\boxed{r=-1}
\]
does not define a series.

::: {.proof}
Combine steps <1>29--<1>36.
:::

<1>38. Collecting the six classifications:
\[
\boxed{
\begin{array}{c|c}
\text{Series} & \text{Behavior}\\
\hline
1 & \text{converges for }0<p<1;\ \text{diverges for }p\ge1\\
2 & \text{absolute if }p>\frac12;\ \text{conditional if }-\frac12<p\le\frac12;\ \text{divergent if }p\le-\frac12\\
3 & \text{converges iff }p>1\\
4 & \text{converges}\\
5 & \text{converges}\\
6 & \text{absolute if }|r|>1;\ \text{divergent if }|r|<1\text{ or }r=1;\ r=-1\text{ undefined}.
\end{array}}
\]

::: {.proof}
Use steps <1>7, <1>16, <1>21, <1>24, <1>28, and <1>37.
:::

<1>39. Q.E.D.

::: {.proof}
Step <1>38 gives the complete convergence classification.
:::
:::
