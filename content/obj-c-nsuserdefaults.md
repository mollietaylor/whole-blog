Title: NSUserDefaults Example with NSMutableArray
Date: 2015-01-18
Tags: Objective-C, NSUserDefaults, Core Data, NSKeyedArchiver, setObject forKey, arrayForKey, NSMutableArray, mutableCopy
Category: Objective-C
Slug: nsuserdefaults
Author: Mollie Taylor
Summary: I was misinformed that to have information persist between app uses, you had to either use Core Data or a cloud backend. Boy, was I ever wrong. It's so much easier than that!

I was misinformed that to have information persist between app uses, you had to either use Core Data or a cloud backend. Boy, was I ever wrong. It's so much easier than that!

From [NSHipster](http://nshipster.com/nscoding/):

![NSHipster's opinion]({filename}/images/nsuserdefaults-nshipster.png){.size-auto}

In this case, we're going to be doing something even easier than the full ```NSKeyedArchiver```. For this blog post, we'll be creating a very simple array example for using ```NSUserDefaults``` to persistently store data. We'll be able to add items to and remove items from the array.


* Start a new Single View Application project.
* Delete ```ViewController.h``` and ```ViewController.m```.
* Remove the View Controller from the storyboard.
* Make a new file that is a subclass of ```UITableViewController```. Name it ```ItemTVC```.
* Drag a Table View Controller into the storyboard and make it the Initial View Controller (in the Attributes inspector). Give it the class ```ItemTVC```. Give the cell the identifier "```Cell```".
* Leave ```ItemTVC.h``` as it is and work in ```ItemTVC.m```.

In ```viewDidLoad```:

	:::obj-c
	- (void)viewDidLoad {
	    [super viewDidLoad];
	    
	    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
	    
	    self.array = [[defaults arrayForKey:@"array"] mutableCopy];

	}

```NSUserDefaults``` will always return an immutable version of any object you pass it. As a result, we need to use ```mutableCopy``` before using the array we've retrieved from ```NSUserDefaults```.

In ```(IBAction)addItem``` (storyboard for add item button) or ```insertNewObject``` (code for add item button) or similar:

	:::obj-c
	// if you aren't using storyboard, this might be insertNewObject or a similar method instead of an IBAction
	- (IBAction)addItem:(id)sender {
	    
	    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
	    
	    if ([self.array count] == 0) {
	        self.array = [[NSMutableArray alloc] init];
	    }
	    
	    [self.array addObject:[NSDate date]];
	    [defaults setObject:self.array forKey:@"array"];
	    [self.tableView reloadData];

	}

In ```cellForRowAtIndexPath```:

	- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
	    
	    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"Cell" forIndexPath:indexPath];
	    
	    NSDate *item = self.array[indexPath.row];
	    cell.textLabel.text = [item description];
	    
	    return cell;
	}

This step is optional. If you want to be able to remove items, add this in ```commitEditingStyle forRowAtIndexPath```. 

	- (void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle forRowAtIndexPath:(NSIndexPath *)indexPath {
	    
	    if (editingStyle == UITableViewCellEditingStyleDelete) {
	        
	        NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
	        
	        [self.array removeObjectAtIndex:indexPath.row];
	        [defaults setObject:self.array forKey:@"array"];
	        [self.tableView reloadData];
	        
	    }
	    
	}

[The full code is available on Github](https://github.com/mollietaylor/NSUserDefaults-Example/tree/cd562c1a72410fd4e09071af265fe510c1200725).

##References
* <http://nshipster.com/nscoding/>
* <https://www.udemy.com/complete-ios-developer-course/#/>
* <http://stackoverflow.com/questions/19634426/how-to-save-nsmutablearray-in-nsuserdefaults>
