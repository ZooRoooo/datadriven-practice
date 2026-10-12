def parse_address(address: str) -> dict:
  # 1. Split the string into 3 parts using commas
  parts = address.split(",")
    
  # 2. Extract each section and remove extra leading/trailing spaces
  street = parts[0].strip()
  city = parts[1].strip()
    
  # 3. Split the state and zip by space
  state_zip = parts[2].strip().split()
  state = state_zip[0]
  zip_code = state_zip[1]  # Keep as string to retain leading zeroes
    
  return {
    "zip": zip_code,
    "city": city,
    "state": state,
    "street": street
  }
