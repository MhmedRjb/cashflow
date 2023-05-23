
import pandas as pd
from Dataprocessor import DataProcessor

def test_ApplyDICtToCol():
    # Create an instance of the DataProcessor class
    dp = DataProcessor(file_path='some_file_path', expected_cols=3)
    
    # Set the data attribute of the dp instance to a sample data frame
    dp.data = pd.DataFrame({"a":[1,2,3],"b":[2,3,4],"c":[3,4,5]})
    
    # Create an expected data frame
    expected_df = pd.DataFrame({"a":[1,2,3],"b":[2,3,4],"c":[3,4,5]})
    expected_df["a"] = expected_df["a"].replace({1:0})
    expected_df["b"] = expected_df["b"].replace({2:0,3:1})
    expected_df["c"] = expected_df["c"].replace({2:0,4:1,5:2})

    # Call the ApplyDICtToCol method on the dp instance with specific arguments
    dp.ApplyDICtToCol("a",{1:0})
    dp.ApplyDICtToCol("b",{2:0,3:1})
    dp.ApplyDICtToCol("c",{3:0,4:1,5:2})
    
    # Check if the resulting data attribute of the dp instance is equal to the expected data frame
    pd.testing.assert_frame_equal(dp.data, expected_df)

print(test_ApplyDICtToCol())