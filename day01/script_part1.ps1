$puzzle_input = Get-Content -Path ./puzzle_input.txt

$puzzle_result = 0

foreach ($line in $puzzle_input) {
    $puzzle_result += [int](@([RegEx]::Matches($line,"\d{1}").Value[0], [RegEx]::Matches($line,"\d{1}").Value[-1]) -join "")
}

Write-Output "Result: $puzzle_result"
