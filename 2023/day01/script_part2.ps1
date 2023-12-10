$puzzle_input = Get-Content -Path ./puzzle_input.txt

$puzzle_result = 0

function AugmentLine {
    param (
        [String]$Line
    )

    $_replacements = ${
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
        six = 6
        seven = 7
        eight = 8
        nine = 9
    }
    Enum Replacements {
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
        six = 6
        seven = 7
        eight = 8
        nine = 9
    }

    $_line = $Line

    while ([RegEx]::Matches($_line,"(one|two|three|four|five|six|seven|eight|nine)")) {
        $_matches = [RegEx]::Matches($_line,"(one|two|three|four|five|six|seven|eight|nine)")
        $_match = $_matches | Sort-Object Index | Select-Object -First 1
        

    }
    [RegEx]::Matches($_line,"(one|two|three|four|five|six|seven|eight|nine)")

    foreach ($_replacement in $_replacements) {
        $Line.IndexOf()
    }
    
}

# foreach ($line in $puzzle_input) {
#     $puzzle_result += [int](@([RegEx]::Matches($line,"\d{1}").Value[0], [RegEx]::Matches($line,"\d{1}").Value[-1]) -join "")
# }

Write-Output "Result: $puzzle_result"
