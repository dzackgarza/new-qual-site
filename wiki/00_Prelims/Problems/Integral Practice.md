---
order: 100002
---

# Integral Sheet

Here is a [youtube video](https://www.youtube.com/watch?v=dgm4-3-Iv3s) that potentially has many more integrals.

Note: some of these were incorrect, and the solutions need to all be checked in detail.

Techniques to cover, in order of difficulty:

- Elementary antiderivatives

  - Exponentials, polynomials, trig functions, logs

- u-substitutions

- Trig identities

  - e.g. $\displaystyle \int \cos^2(x) = \displaystyle \int \frac 1 2 (1 + \cos(2x))$

- Trigonometric substitutions

- Partial Fraction Decomposition

- Reverse chain rule

  - e.g. $\displaystyle \int \tan(x)$

- Integration by parts

  - e.g. $\displaystyle \int x^2 e^x$

- "Periodic" integration by parts

  - e.g. $\displaystyle \int e^x \sin(x)$

- Products of powers of trigonometric functions

  - e.g. $\displaystyle \int \sin^3(x)\cos^2(x)$

- u-sub with a back-substitution

  - e.g. $\displaystyle \int \frac{1}{x-3\sqrt{x+10}}, u=\sqrt{x+10} \implies x = u^2-10$

- Trionometric reduction formulas

  - e.g. $\displaystyle \int \sec^3 x$

- Completing the square

  - e.g. $\displaystyle \int \sqrt{x^2+4x+5} = \displaystyle \int \sqrt{(x+2)^2 + 1}$, then trig sub

- Polynomial long division

- Exotic antiderivatives

  - e.g. $\displaystyle \int e^x + e^{-x} = \displaystyle \int 2\cosh(x)$

- Product to sum formulas

- Shoelace method of integration by parts

- Weierstrass substitution

  - e.g. $\displaystyle \int \frac 1 {1 + \sin(x)}, \sin(x) = \frac{2t}{1+t^2}$ wher $t=\tan(\frac x 2)$

- "Rigged" integration by parts

  - e.g. for $\displaystyle \int f(x) dx$, let $u=f(x), v' = 1$

- Integrating even/odd functions over symmetric domains

  - e.g. $\displaystyle \int_{-1}^1 \sin(x)$

- Bonus round: $\displaystyle \int_\mathbb{R} e^{-x^2}$

  - Every math student should know one way of deriving this.
    :)

## Definitions

##### Level 1

1. $\displaystyle \int x^a ~dx = \frac {x^{a+1}}{a+1}$

2. $\displaystyle \int a^{bx} ~dx = \frac {a^{bx}}{b \ln (a)}$

[[P-JHXZS]] 3. $\displaystyle \int \frac {1}{x} ~dx = \ln (x)​$

4. $\displaystyle \int \sin (ax) ~dx = - \frac {1}{a} \cos (ax)$

   $\displaystyle \int \cos (ax) ~dx = \frac {1}{a} \sin (ax)$

   $\displaystyle \int \tan (ax) ~dx = - \frac {1}{a} \ln (\cos (ax))$

[[P-OSVPH]] $\displaystyle \int \cot (ax) ~dx = \frac {1}{a} \ln (\sin (ax))​$

$\displaystyle \int \sec (ax) ~dx = \frac {1}{a} \ln (\sec (ax) + \tan (ax))​$

$\displaystyle \int \csc (ax) ~dx = - \frac {1}{a} \ln (\csc (ax) + \cot (ax))$

5. $\displaystyle \int \cos (ax) ~dx = \frac {1}{a} \sin (ax)$

   $\displaystyle \int \sin (ax) ~dx = - \frac {1}{a} \cos (ax)$

   $\displaystyle \int \sec ^2 (ax) ~dx = \frac {1}{a} \tan (ax)​$

   $\displaystyle \int \csc ^2 (ax) ~dx = - \frac {1}{a} \cot (ax)$

   $\displaystyle \int \sec (ax) \tan (ax) ~dx = \frac {1}{a} \sec (ax)$

[[P-KAQ4G]]

[[P-73DDS]] 6. $\displaystyle \int \frac {1}{\sqrt {a^2-x^2}}~dx = \sin ^{-1} (\frac {x}{a})$

1. $\displaystyle \int \frac {1}{\sqrt {4-9x^2}} ~dx = \color {blue} {\frac {1}{3}\sin ^{-1} (\frac {3}{2} x)}$

- **Solution:** $\frac {1}{\sqrt {4-9x^2}} = \frac {1}{3 \sqrt {(\frac {2}{3})^2 - x^2}}$

$\displaystyle \int \frac {1}{x^2+a^2}~dx = \frac {1}{a} \tan ^{-1} (\frac {x}{a})$

[[P-UGR7G]] $\displaystyle \int \frac {1}{x \sqrt {x^2 - 1}} ~dx = \sec ^{-1} (x)$

[[P-7NXQ7]] 7. $\displaystyle \int \sin^{-1}(x) ~dx = x\sin^{-1}(x) + \sqrt {1 - x^2}$

- **Used 2018**, *Unsolved*

$\displaystyle \int \tan^{-1}(x) ~dx = x \tan^{-1}(x) - \frac {1}{2} \ln (x^2 + 1)$

$\displaystyle \int \sec ^{-1} (x) ~dx = x \sec ^{-1} (x) - \ln (\sqrt {x^2 - 1} + x)$

## Easy

##### Level 1

1. $\displaystyle \int \frac {\sin^2(2x)}{1+\cos(2x)} ~dx = \color{blue} {x-\cos(x)\sin(x)}$

- **Solution:** $\frac {\sin ^2 (2x)}{1 + \cos (2x)} = \frac {1 - \cos ^2 (2x)}{1 + \cos (2x)} = 1 - \cos (2x)$

- **Used 2019**

[[P-75G3E]] [[P-3MDGM]] [[P-UOENS]] [[P-R4I5W]]

[[P-7X6ZK]]

## Interesting tricks

##### Level 1

###### Change the order of integration

[[P-E5WUU]]

##### Level 2

###### Odd funtion

1. $\displaystyle \int_{-\pi}^{\pi} e^{-x^2}\sin (x) dx = \color {blue} {0}$

2. $\displaystyle \int_{-1729}^{1729} \sin^5(x^3) + \sin^3(x^5) + x = \color {blue} {0}$

##### Level 3

###### Gaussian distribution

[[P-H442E]]

###### Reverse Quotient Rule

[[P-ANJIW]]

## u-Substitutions

##### Level 1

[[P-D75SD]] [[P-5RLR6]]

[[P-Y6XVP]] [[P-IOAQB]]

[[P-DH6CX]] [[P-EAYXF]] [[P-TO7UO]] [[P-UNHGI]] [[P-XIKRI]] [[P-4GVRD]] [[P-UVSXF]] [[P-5DV7Z]] [[P-JIAQR]] [[P-SZNKD]]

##### Level 2

[[P-MKEL2]] [[P-PV5GI]]

##### Level 3

[[P-XYIBX]] [[P-B6FMH]]

## Trigonometric Substitution

##### Level 2

###### Sin

[[P-PHHXJ]] [[P-45Y6B]] [[P-5OCGZ]] [[P-UUACQ]]

###### Sec

[[P-5UMRG]] [[P-SUXVR]]

###### Tan

[[P-XRZVW]]

##### Level 3

[[P-OY6YK]]

## Integration by Parts

##### Level 1

[[P-SAFVA]] [[P-SQVNA]] [[P-2ALGH]] [[P-GLK4G]]

[[P-NKCDN]]

##### Level 2

[[P-YFZRX]] [[P-E6Y7R]]

##### Level 3

[[P-VYOWN]] [[P-NM425]]

## Partial Fraction Decomposition

##### Level 1

[[P-FDWKY]]

##### Level 2

[[P-7CUNN]]

##### Level 3

[[P-PAVWJ]]

## Powers of Sine and Cosine

##### Trick

$\displaystyle \int \sin ^n (x) ~dx = \frac {n - 1}{n} \int \sin ^{n - 2} (x) ~dx - \frac {1}{n} \cos (x) \sin ^{n - 1} (x)$

$\displaystyle \int \cos ^n (x) ~dx = \frac {n - 1}{n} \int \cos ^{n - 2} (x) ~dx + \frac {1}{n} \sin (x) \cos ^{n - 1} (x)$

##### Level 2

[[P-RVMWA]]

##### Level 3

[[P-R67LO]]

## Powers of Tangent and Cosecant

##### Trick

$\displaystyle \int \sec ^n (x) ~dx = \frac {n - 2}{n - 1} \int \sec ^{n - 2} (x) ~dx + \frac {1}{n - 1} \tan (x) \sec ^{n - 2} (x)$

##### Level 3

[[P-F6K7Y]]

## Products to Sum / Sums to Product formulas

##### Trick

$\sin (x) + \sin (y) = 2 \sin (\frac {x + y}{2}) \cos (\frac {x - y}{2})$

$\sin (x) - \sin (y) = 2 \cos (\frac {x + y}{2}) \sin (\frac {x - y}{2})​$

[[P-PC2H7]]

##### Level 1

[[P-CJ16Y]]

## Weierstauss substitution

##### Trick

Let $u = \tan (\frac {x}{2})$

Then, $\sin (x) = \frac {2u}{1 + u^2}​$, $\cos (x) = \frac {1 - u^2}{1 + u^2}​$, $dx = \frac {2}{1 + u^2} ~du​$

##### Level 3

[[P-EQFMD]]

##### Level 4

[[P-NHFXM]]

## Combined Techniques

##### Level 3

[[P-W6TOK]]

## Too Hard

[[P-E7N6V]]
