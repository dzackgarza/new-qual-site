---
schema: qual/card@1
id: P-PRACT20-W6-27
kind: problem
title: Tracing the Euclidean algorithm and two integer loops
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
What is the output of the following algorithms?

(A)
```text
a = 273
b = 110
while b > 0
    r = a (mod b)
    a = b
    b = r
    print r
end
```

(B)
```text
n = 88
i = 1
while i < n
    i = i+1
    k = n
    while k >= i
        if i=k then print i
        k = k - 1
    end
end
```

(C)
```text
n = 123456
while n > 0
    j = n (mod 100)
    print j
    n = floor(n/100)
end
```
:::

## Part (A)

::: pf

::: pf-step

Initially,
\[
a=273,
\qquad
b=110.
\]
The first remainder is
\[
\boxed{
273\bmod110=53}.
\]


::: pf-proof

\[
273=2\cdot110+53.
\]
The algorithm then sets
\[
a=110,
\qquad
b=53
\]
and prints \(53\).

:::

:::

::: pf-step

The next remainder is
\[
\boxed{
110\bmod53=4}.
\]


::: pf-proof

\[
110=2\cdot53+4.
\]
The algorithm sets
\[
a=53,
\qquad
b=4
\]
and prints \(4\).

:::

:::

::: pf-step

The next remainder is
\[
\boxed{
53\bmod4=1}.
\]


::: pf-proof

\[
53=13\cdot4+1.
\]
The algorithm sets
\[
a=4,
\qquad
b=1
\]
and prints \(1\).

:::

:::

::: pf-step

The final remainder is
\[
\boxed{
4\bmod1=0}.
\]


::: pf-proof

\[
4=4\cdot1+0.
\]
The algorithm sets
\[
a=1,
\qquad
b=0
\]
and prints \(0\).

:::

:::

::: pf-step

The loop then stops.


::: pf-proof

Its condition is
\[
b>0.
\]
After step <1>4, \(b=0\).

:::

:::

::: pf-step

Hence the output of (A) is
\[
\boxed{
53,\ 4,\ 1,\ 0}.
\]


::: pf-proof

These are the values printed in steps <1>1--<1>4.

:::

:::

::: pf-step

At the start of each outer-loop iteration, \(i<88\), and the first
operation is
\[
i=i+1.
\]


::: pf-proof

This is the first command inside the outer loop.

:::

:::

::: pf-step

Therefore the values of \(i\) used by the inner loop are
\[
\boxed{
2,3,\dots,88}.
\]


::: pf-proof

The initial value is \(i=1\). Each outer iteration increases it by one before
the inner loop begins. When \(i=87\) at the outer-loop test, the loop runs
once more and changes \(i\) to \(88\). The next outer-loop test fails because
\(88<88\) is false.

:::

:::

::: pf-step

Fix one such value of \(i\). The inner loop starts with
\[
k=88
\]
and decreases \(k\) by one until \(k<i\).


::: pf-proof

This is exactly the assignment and loop condition
\[
k=88,
\qquad
\texttt{while }k\ge i,
\qquad
k=k-1.
\]

:::

:::

::: pf-step

During that inner loop, the equality
\[
k=i
\]
occurs exactly once.


::: pf-proof

The integer \(k\) takes the values
\[
88,87,\dots,i
\]
once each before being decremented to \(i-1\), which terminates the loop.

:::

:::

::: pf-step

Hence the inner loop prints the current value of \(i\) exactly once.


::: pf-proof

The print command is executed precisely when
\[
i=k,
\]
which occurs exactly once by step <1>10.

:::

:::

::: pf-step

Therefore the output of (B) is
\[
\boxed{
2,3,4,\dots,88}.
\]


::: pf-proof

Apply step <1>11 to the successive outer-loop values listed in step <1>8.

:::

:::

::: pf-step

Initially,
\[
n=123456.
\]
Thus
\[
\boxed{
n\bmod100=56}.
\]


::: pf-proof

\[
123456
=
1234\cdot100+56.
\]
The algorithm prints \(56\), then replaces \(n\) by
\[
\left\lfloor\frac{123456}{100}\right\rfloor
=
1234.
\]

:::

:::

::: pf-step

With
\[
n=1234,
\]
one has
\[
\boxed{
n\bmod100=34}.
\]


::: pf-proof

\[
1234
=
12\cdot100+34.
\]
The algorithm prints \(34\), then replaces \(n\) by
\[
\left\lfloor\frac{1234}{100}\right\rfloor
=
12.
\]

:::

:::

::: pf-step

With
\[
n=12,
\]
one has
\[
\boxed{
n\bmod100=12}.
\]


::: pf-proof

Since
\[
12<100,
\]
its remainder modulo \(100\) is \(12\). The algorithm prints \(12\), then
replaces \(n\) by
\[
\left\lfloor\frac{12}{100}\right\rfloor
=
0.
\]

:::

:::

::: pf-step

The loop then stops.


::: pf-proof

Its condition is
\[
n>0,
\]
and step <1>15 leaves \(n=0\).

:::

:::

::: pf-step

Hence the output of (C) is
\[
\boxed{
56,\ 34,\ 12}.
\]


::: pf-proof

These are the printed values from steps <1>13--<1>15.

:::

:::

::: pf-qed

Steps <1>6, <1>12, and <1>17 give the outputs of (A), (B), and (C),
respectively.

:::

:::
