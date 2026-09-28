---
order: 21
---

# Integral practice

A video with further integrals: [integration practice](https://www.youtube.com/watch?v=dgm4-3-Iv3s).

## Techniques

- Elementary antiderivatives of exponentials, polynomials, trigonometric functions, and logarithms

- $u$-substitution

- Trigonometric identities, for example $\int \cos^2 x\dx = \int \frac 1 2 (1 + \cos 2x)\dx$

- Trigonometric substitution

- Partial fraction decomposition

- Recognizing $g'(x)/g(x)$, for example $\int \tan x\dx = -\ln\abs{\cos x} + C$

- Integration by parts, for example $\int x^2 e^x\dx$

- Integration by parts in which the original integral reappears, for example $\int e^x \sin x\dx$

- Products of powers of trigonometric functions, for example $\int \sin^3 x\cos^2 x\dx$

- $u$-substitution followed by solving for $x$, for example $\int \frac{\dx}{x-3\sqrt{x+10}}$ with $u=\sqrt{x+10}$ and $x = u^2-10$

- Trigonometric reduction formulas, for example $\int \sec^3 x\dx$

- Completing the square, for example $\int \sqrt{x^2+4x+5}\dx = \int \sqrt{(x+2)^2 + 1}\dx$, followed by trigonometric substitution

- Polynomial long division

- Hyperbolic functions, for example $\int (e^x + e^{-x})\dx = \int 2\cosh x\dx$

- Product-to-sum formulas

- The tabular method for integration by parts

- The Weierstrass substitution, for example $\int \frac{\dx}{1 + \sin x}$ with $t=\tan\frac x2$ and $\sin x = \frac{2t}{1+t^2}$

- Integration by parts with $u=f(x)$ and $dv = \dx$, for $\int f(x) \dx$

- Odd and even functions integrated over symmetric intervals, for example $\int_{-1}^1 \sin x\dx = 0$

- The Gaussian integral $\int_\RR e^{-x^2}\dx = \sqrt\pi$

## Standard antiderivatives

In each formula, $a\neq0$, and the constant of integration is omitted.

1. $\displaystyle \int x^r \dx = \frac {x^{r+1}}{r+1}$ for $r\neq-1$, and $\displaystyle \int \frac {1}{x} \dx = \ln \abs x$.

2. $\displaystyle \int b^{cx} \dx = \frac {b^{cx}}{c \ln b}$ for $b>0$, $b\neq1$, $c\neq0$.

[[P-JHXZS]]

3. Trigonometric functions:
   $$
   \begin{aligned}
   \int \sin (ax) \dx &= - \frac {1}{a} \cos (ax), & \int \cos (ax) \dx &= \frac {1}{a} \sin (ax), \\
   \int \tan (ax) \dx &= - \frac {1}{a} \ln \abs{\cos (ax)}, & \int \cot (ax) \dx &= \frac {1}{a} \ln \abs{\sin (ax)}, \\
   \int \sec (ax) \dx &= \frac {1}{a} \ln \abs{\sec (ax) + \tan (ax)}, & \int \csc (ax) \dx &= - \frac {1}{a} \ln \abs{\csc (ax) + \cot (ax)}, \\
   \int \sec ^2 (ax) \dx &= \frac {1}{a} \tan (ax), & \int \csc ^2 (ax) \dx &= - \frac {1}{a} \cot (ax), \\
   \int \sec (ax) \tan (ax) \dx &= \frac {1}{a} \sec (ax). & &
   \end{aligned}
   $$

[[P-OSVPH]]

[[P-KAQ4G]]

4. Inverse trigonometric functions, for $a>0$:
   $$
   \int \frac {\dx}{\sqrt {a^2-x^2}} = \sin ^{-1} \frac {x}{a}, \qquad
   \int \frac {\dx}{x^2+a^2} = \frac {1}{a} \tan ^{-1} \frac {x}{a}, \qquad
   \int \frac {\dx}{x \sqrt {x^2 - 1}} = \sec ^{-1} x \quad (x>1).
   $$

[[P-73DDS]]

::: {.example}
$$
\int \frac {\dx}{\sqrt {4-9x^2}} = \frac {1}{3}\sin ^{-1} \left(\frac {3}{2} x\right),
$$
since $\sqrt {4-9x^2} = 3 \sqrt {(2/3)^2 - x^2}$.
:::

[[P-UGR7G]]

5. Antiderivatives of inverse trigonometric functions:
   $$
   \begin{aligned}
   \int \sin^{-1}x \dx &= x\sin^{-1}x + \sqrt {1 - x^2}, \\
   \int \tan^{-1}x \dx &= x \tan^{-1}x - \frac {1}{2} \ln (x^2 + 1), \\
   \int \sec ^{-1} x \dx &= x \sec ^{-1} x - \ln \left(x + \sqrt {x^2 - 1}\right) \quad (x>1).
   \end{aligned}
   $$

[[P-7NXQ7]]

## Simplification

::: {.example}
$$
\int \frac {\sin^2(2x)}{1+\cos(2x)} \dx = x-\sin x\cos x + C,
$$
since $\frac {\sin ^2 (2x)}{1 + \cos (2x)} = \frac {1 - \cos ^2 (2x)}{1 + \cos (2x)} = 1 - \cos (2x)$.
:::

[[P-75G3E]] [[P-3MDGM]] [[P-UOENS]] [[P-R4I5W]]

[[P-7X6ZK]]

## Other methods

### Changing the order of integration

[[P-E5WUU]]

### Odd functions

::: {.example}
The integrands below are odd, so
$$
\int_{-\pi}^{\pi} e^{-x^2}\sin x \dx = 0, \qquad \int_{-1729}^{1729} \left(\sin^5(x^3) + \sin^3(x^5) + x\right)\dx = 0.
$$
:::

### The Gaussian integral

[[P-H442E]]

### Quotient rule in reverse

[[P-ANJIW]]

## $u$-substitution

[[P-D75SD]] [[P-5RLR6]]

[[P-Y6XVP]] [[P-IOAQB]]

[[P-DH6CX]] [[P-EAYXF]] [[P-TO7UO]] [[P-UNHGI]] [[P-XIKRI]] [[P-4GVRD]] [[P-UVSXF]] [[P-5DV7Z]] [[P-JIAQR]] [[P-SZNKD]]

[[P-MKEL2]] [[P-PV5GI]]

[[P-XYIBX]] [[P-B6FMH]]

## Trigonometric substitution

### $x = a\sin\theta$

[[P-PHHXJ]] [[P-45Y6B]] [[P-5OCGZ]] [[P-UUACQ]]

### $x = a\sec\theta$

[[P-5UMRG]] [[P-SUXVR]]

### $x = a\tan\theta$

[[P-XRZVW]]

[[P-OY6YK]]

## Integration by parts

[[P-SAFVA]] [[P-SQVNA]] [[P-2ALGH]] [[P-GLK4G]]

[[P-NKCDN]]

[[P-YFZRX]] [[P-E6Y7R]]

[[P-VYOWN]] [[P-NM425]]

## Partial fraction decomposition

[[P-FDWKY]]

[[P-7CUNN]]

[[P-PAVWJ]]

## Powers of sine and cosine

For $n\geq 2$,
$$
\begin{aligned}
\int \sin ^n x \dx &= \frac {n - 1}{n} \int \sin ^{n - 2} x \dx - \frac {1}{n} \cos x \sin ^{n - 1} x, \\
\int \cos ^n x \dx &= \frac {n - 1}{n} \int \cos ^{n - 2} x \dx + \frac {1}{n} \sin x \cos ^{n - 1} x.
\end{aligned}
$$

[[P-RVMWA]]

[[P-R67LO]]

## Powers of secant

For $n\geq 2$,
$$
\int \sec ^n x \dx = \frac {n - 2}{n - 1} \int \sec ^{n - 2} x \dx + \frac {1}{n - 1} \tan x \sec ^{n - 2} x.
$$

[[P-F6K7Y]]

## Sum-to-product and product-to-sum formulas

$$
\sin x + \sin y = 2 \sin \frac {x + y}{2} \cos \frac {x - y}{2}, \qquad
\sin x - \sin y = 2 \cos \frac {x + y}{2} \sin \frac {x - y}{2}.
$$

[[P-PC2H7]]

[[P-CJ16Y]]

## The Weierstrass substitution

With $u = \tan \frac {x}{2}$,
$$
\sin x = \frac {2u}{1 + u^2}, \qquad \cos x = \frac {1 - u^2}{1 + u^2}, \qquad \dx = \frac {2}{1 + u^2} \, du.
$$

[[P-EQFMD]]

[[P-NHFXM]]

## Combined techniques

[[P-W6TOK]]

## Further integrals

[[P-E7N6V]]
