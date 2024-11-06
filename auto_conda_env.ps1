function Set-CondaEnv {
    $envsPath = "D:\miniforge3\envs"
    $currentDir = Get-Location

    # Write-Output "DEBUG: Environment path being checked: $envsPath"
    # Write-Output "DEBUG: Current directory: $($currentDir.Path)"

    # Check if envsPath exists
    if (Test-Path $envsPath) {
        # Write-Output "DEBUG: Conda envs directory exists"
    } else {
        # Write-Output "DEBUG: WARNING - Conda envs directory not found at $envsPath"
    }

    # Only activate/deactivate in D:\workspace directory
    if ($currentDir.Path -like "D:\workspace*") {
        # Write-Output "DEBUG: Currently in workspace directory"
        $currentDirName = Split-Path -Leaf $currentDir
        # Write-Output "DEBUG: Current directory name: $currentDirName"

        # Check if there is a Conda environment matching the current directory name
        $envPath = "$envsPath\$currentDirName"
        # Write-Output "DEBUG: Checking for environment at: $envPath"

        if (Test-Path "$envsPath\$currentDirName") {
            # Write-Output "DEBUG: Found matching environment directory"
            try {
                & conda activate $currentDirName
                # Write-Output "Activated Conda environment: $currentDirName"
            } catch {
                Write-Output "DEBUG: Error activating environment: $_"
            }
        } else {
            # Write-Output "DEBUG: No matching environment found at $envPath"
            try {
                & conda deactivate
                # Write-Output "No matching environment. Deactivated Conda environment."
            } catch {
                Write-Output "DEBUG: Error deactivating environment: $_"
            }
        }
    } else {
        # Write-Output "DEBUG: Not in workspace directory: $($currentDir.Path)"
        try {
            & conda deactivate
            # Write-Output "Not in D:\workspace. Deactivated Conda environment."
        } catch {
            Write-Output "DEBUG: Error deactivating environment: $_"
        }
    }
}

# Override Set-Location to trigger Set-CondaEnv on directory change
function Set-Location {
    param([string]$path)
    # Write-Output "DEBUG: Changing directory to: $path"
    try {
        Microsoft.PowerShell.Management\Set-Location -LiteralPath $path
        # Write-Output "DEBUG: Directory change successful"
        Set-CondaEnv
    } catch {
        Write-Output "DEBUG: Error changing directory: $_"
    }
}

# Run Set-CondaEnv initially
# Write-Output "DEBUG: Running initial Set-CondaEnv"
Set-CondaEnv
# "commandline": "%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",