# Publicar en GitHub

## 1. Verificar secretos

Antes del primer commit:

```bash
grep -RInE "SIMPLEAPI_KEY|SII_CERT_PASS|\\.pfx|\\.p12|Authorization|token|password|secret" .
find . -type f \\( -name "*.xml" -o -name "*.pdf" -o -name "*.pfx" -o -name "*.p12" \\)
```

Debe quedar claro que no hay:

- `.env`
- certificados
- CAF reales
- XML reales
- PDF reales
- claves o tokens

## 2. Inicializar repo

```bash
git init
git add .
git status
git commit -m "Initial public SII certification guide"
```

## 3. Crear repo en GitHub

Opcion con GitHub CLI:

```bash
gh repo create sii-certificacion-simpleapi --public --source=. --remote=origin --push
```

Opcion manual:

1. Crear repo vacio en GitHub.
2. Copiar la URL remota.
3. Ejecutar:

```bash
git remote add origin git@github.com:TU_USUARIO/sii-certificacion-simpleapi.git
git branch -M main
git push -u origin main
```

## 4. Despues de publicar

Revisa GitHub en el navegador y confirma que no aparezcan datos reales.

Si por accidente subiste un secreto:

1. Revoca el secreto inmediatamente.
2. Borra el repo o reescribe historia.
3. Considera ese secreto comprometido.
