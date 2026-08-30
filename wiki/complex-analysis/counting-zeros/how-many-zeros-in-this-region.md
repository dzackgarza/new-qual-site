---
title: How many zeros in this region?
order: 0
problems:
  topics:
  - Zeros
  - Zeros of Holomorphic Functions
  - Zeros of Polynomials
  - Polynomial Roots
  - Polynomials
---

# How many zeros in this region?

Counting the zeros of a function in a region is one exam question with three standard answers, and choosing between them is the whole difficulty.
The choice is made on what you are handed, not on what the theorems say.

## Can you just factor it?

Try this first, and on a polynomial of low degree it often ends the problem.
A zero you can name is worth more than a zero you have counted, and multiplicity is read off the factorization.

Two facts that shorten the search:

- A zero of $f$ of multiplicity $m \geq 2$ is a zero of $f'$, and the same holds for $f - a$ at an $a\dash$point.

- $f$ and $f-w$ have the same derivative, so the critical points do not move when you change the value you are counting.

## Does the function split into a big part and a small part?

**Use Rouché.**
This is the case whenever $f$ is a sum whose terms have visibly different sizes on the boundary: a polynomial where one monomial dominates on $\abs z = R$, or an entire function against a polynomial.

Write $f = M + m$, show $\abs{m} < \abs{M}$ on $\gamma$, and count the zeros of $M$, which you chose to be something you can count.
The strategies are on [[complex-analysis/counting-zeros/rouches-theorem|Rouché's theorem]]; the splitting usually changes with the radius, which is why the same polynomial needs a different $M$ on $\abs z < 1$ than on $\abs z < 2$.

Rouché needs a *strict* inequality on the whole boundary curve, and it counts zeros minus poles, so for a meromorphic $f$ read the conclusion carefully.

## Are you given a winding number, or a picture of the image curve?

**Use the argument principle.**
The index version says the count is how many times $f\circ\gamma$ wraps the origin, so a problem that shows you the image of the boundary, or tells you the change in $\arg f$ along it, is asking for this one and nothing else.

It is also the right tool when the question is about zeros *and* poles together, since it is the difference that the integral computes.

## Is the function a limit of functions you already understand?

**Use Hurwitz.**
A sequence $f_n \to f$ locally uniformly, with each $f_n$ nonvanishing (or injective), forces the limit to be nonvanishing (or injective) unless it is constant.
This is how a normal-families argument ends: Montel produces the limit, Hurwitz says the limit kept the property.

## Is the question "exactly one solution of $f(z) = w$"?

Both tools answer it, and Rouché is usually shorter.
Apply Rouché to $f - w$, splitting off the dominant term.
The argument principle answers it through the counting integral
\[
F(w) \da {1\over 2\pi i} \oint_{\bd \Omega} {f'(z) \over f(z) - w} \dz
,\]
which is continuous in $w$ wherever $f \neq w$ on $\bd\Omega$ and integer valued, hence locally constant.
That local constancy is the actual content: the number of solutions cannot change as $w$ moves inside a component.

## The two theorems, side by side

|  | Argument principle | Rouché |
| --- | --- | --- |
| What you must know | $f$ on the boundary, or its image curve | that one term dominates on the boundary |
| What it returns | $\size Z_f - \size P_f$ | $\size Z_f = \size Z_M$ |
| Typical input | a winding number, a change in $\arg$ | a polynomial, or an entire function plus a small term |
| Fails when | you cannot evaluate the integral or see the image | no term dominates, or the inequality is not strict |

Rouché is proved *from* the argument principle, so nothing is lost by reaching for Rouché first; it is the argument principle with the integral already done.
