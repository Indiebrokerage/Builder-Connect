export type ColorTokens = { primary: string; onPrimary: string; surface: string; text: string; success: string; accent: string; };
export type RadiusTokens = { md: string; lg: string; xl: string };
export type SpaceTokens  = { sm: string; md: string; lg: string; xl: string };
export type FontTokens   = { family: string; sizeBase: string; lineBase: string };
export type BrandTokens = { light: { color: ColorTokens; radius: RadiusTokens; space: SpaceTokens; font: FontTokens; };
                            dark:  { color: ColorTokens; radius: RadiusTokens; space: SpaceTokens; font: FontTokens; }; };
export type BrandsMap = Record<string, BrandTokens>;
