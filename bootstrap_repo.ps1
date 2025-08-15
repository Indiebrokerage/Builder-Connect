Param(
  [Parameter(Mandatory=$true)][string]$Remote,
  [string]$Branch = "main"
)
git init
git checkout -b $Branch 2>$null
git add .
git -c user.name="${env:GIT_USER}" -c user.email="${env:GIT_EMAIL}" commit -m "chore(init): Real Estate Conduit Factory one-click repo"
git remote add origin $Remote 2>$null
git remote set-url origin $Remote
git push -u origin $Branch
Write-Host "✅ Repo bootstrapped and pushed to $Remote ($Branch)"
